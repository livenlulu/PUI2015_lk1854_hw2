import urllib2
import sys
import json

buscount1 = 0

if __name__=='__main__':
	MTA_KEY = sys.argv[1]
	BUS_LINE = sys.argv[2]

	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (MTA_KEY, BUS_LINE)
	request = urllib2.urlopen(url)
	data = json.loads(request.read())

	buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
	
	print "Bus Line: ", BUS_LINE

	buscount = len(buses)
	print "Number of Active Buses : ", buscount


	for b in buses:

		Lat = b['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		Lon = b['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
		print "Bus %s is at latitude %s and longitude %s" % (buscount1, Lat, Lon)
		buscount1 += 1

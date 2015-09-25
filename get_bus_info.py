import json
import sys
import csv
import urllib2

if __name__=='__main__':
	MTA_KEY = sys.argv[1]
	BUS_LINE = sys.argv[2]
	
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (MTA_KEY, BUS_LINE)
	request = urllib2.urlopen(url)
	data = json.loads(request.read())
	buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

	with open(sys.argv[3], 'wb') as csvFile:
		writer = csv.writer(csvFile)
		headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
		writer.writerow(headers)

		for b in buses:
			lat = b['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
			lon = b['MonitoredVehicleJourney']['VehicleLocation']['Longitude']

			if b['MonitoredVehicleJourney']['OnwardCalls'] == {}:
				sn = 'N/A'
				ss = 'N/A'

			else:
				sn = b['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
				ss = b['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']

				writer.writerow([lat, lon, sn, ss])

				#print '%s, %s, %s, %s' % (lat, lon, sn, ss)


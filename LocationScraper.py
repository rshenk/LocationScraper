import requests 
import simplejson 

url = requests.get('http://map.wisc.edu/api/v1/tags/')
content = url.content 
response = simplejson.loads(content)

for item in response:
	#print 'ID:' +  str(item['id']) + ' category: ' +  str( item['name'])
	requestURL = requests.get('http://map.wisc.edu/api/v1/tags/' + str(item['id']) + '.geojson')
	locationContent = requestURL.content
	locationResponse = simplejson.loads(locationContent)
	for item in locationResponse: 
		print '+--------------------+'
		print 'Name: ' + str(item['name'])
		print 'Address: ' + str(item['street_address'])
		print 'Latitude/Longitude: ' + str(item['latlng'])
		print 'Description: '
		description = item['description']
		print  description

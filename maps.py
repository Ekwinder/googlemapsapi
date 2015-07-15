"""
in this file, we create a list to store the directions by using the google maps api.
"""
from googlemaps import Client
from HTMLParser import HTMLParser

#code from stackoverflow to remove html tags
class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)

def strip_tags(html):
	s = MLStripper()
	s.feed(html)
	return s.get_data()

## function to get directions using an instance of googlmap.
def Directions(start, end):
	try:
		mapService = Client('AIzaSyDddi5KttOYGnCalNu8M54DUsc1kCKVCrA')

		directions = mapService.directions(start, end)
		x=[]
		for value in directions[0]['legs'][0]['steps']:
			x.append(strip_tags(value['html_instructions']))
		return x	

	except:
		return 'Error'
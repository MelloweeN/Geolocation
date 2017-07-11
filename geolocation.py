# -*- coding: utf-8 -*-
__author__ = "Max Sandoval Miranda"
__copyright__ = "Copyright (C) 2017"
__license__ = "Public Domain"
__version__ = "1.0"

import json
import csv
import requests

#Get the Key from developers.google.com
key = 'AIzaSyB0lmXXXXXXXXXXXXXXXXXXXMeM'

ifile = open('list.csv', 'rb')
reader = csv.reader(ifile)

new_rows_list = []
new_rows_list.append(['Id','Direccion','Ciudad','Region','Latitud','Longitud'])
for row in reader:
	if row[1]:
		url = "https://maps.googleapis.com/maps/api/geocode/json?key="+key+"&address="+row[1]+" "+row[2]+" "+row[3]
		json = requests.get(url).json()

		lat = str(json['results'][0]['geometry']['location']['lat'])
		lon = str(json['results'][0]['geometry']['location']['lng'])
	else:
		lat = ''
		lon = ''

	new_rows_list.append([row[0],row[1],row[2],row[3],lat,lon])


# Do the writing
file2 = open('list-geolocation.csv', 'wb')
writer = csv.writer(file2)
writer.writerows(new_rows_list)
file2.close()

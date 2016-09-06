import csv

# import mysql.connector
# from mysql.connector import errorcode

# try:
# 	conn = mysql.connector.connect(
# 			user='root',
# 			password='Valya31131',
# 			host='localhost',
# 			database='hotels')
# 	print('It works!')
# except mysql.connector.Error as e:
# 	if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
# 		print("Something is wrong with username or password!")
# 	elif e.errno == errorcode.ER_BAD_DB_ERROR:
# 		print('DataBase Does not exists')
# 	else:
# 		print(e)
# cur = conn.cursor()

i = 0
Country = input('Введите страну: ')

headers = ['Campaign', 'Campaign Daily Budget', 'Languages', 'Location ID', 'Location', 'Networks',
		   'Ad Group', 'Max CPC', 'Flexible Reach', 'Keyword', 'Type', 'Bid adjustment',
		   'Headline', 'Description Line 1', 'Description Line 2', 'Sitelink text', 'Display URL',
		   'Final URL', 'Platform targeting', 'Device Preference', 'Ad Schedule']
print(headers)

line1 = {'Campaign': Country, 'Campaign Daily Budget': '1000', 'Languages': 'ru', 'Location ID': '',
		 'Location': 'Russia', 'Networks': 'Google Search;Search Partners', 'Ad Group': '', 'Max CPC': 0,
		 'Flexible Reach': 0, 'Keyword': 0, 'Type': 0, 'Bid adjustment': 0, 'Headline': 0, 'Description Line 1': 0,
		 'Description Line 2': 0, 'Sitelink text': 0, 'Display URL': 0, 'Final URL': 0, 'Platform targeting': 0,
		 'Device Preference': 0, 'Ad Schedule': 0}
line2 = {'Campaign': Country, 'Campaign Daily Budget': 0, 'Languages': 'ru', 'Location ID': 0,
		 'Location': "Moscow,Moscow,Russia", 'Networks': 0, 'Ad Group': 0, 'Max CPC': 0, 'Flexible Reach': 0,
		 'Keyword': 0, 'Type': 0, 'Bid adjustment': '0', 'Headline': 0, 'Description Line 1': 0,
		 'Description Line 2': 0, 'Sitelink text': 0, 'Display URL': 0, 'Final URL': 0, 'Platform targeting': 0,
		 'Device Preference': 0, 'Ad Schedule': 0}
line3 = {'Campaign': Country, 'Campaign Daily Budget': 0, 'Languages': 0, 'Location ID': 0,
		 'Location': "Moscow Oblast,Russia", 'Networks': 0, 'Ad Group': 0, 'Max CPC': 0, 'Flexible Reach': 0,
		 'Keyword': 0, 'Type': 0, 'Bid adjustment': '100', 'Headline': 0, 'Description Line 1': 0,
		 'Description Line 2': 0, 'Sitelink text': 0, 'Display URL': 0, 'Final URL': 0, 'Platform targeting': 0,
		 'Device Preference': 0, 'Ad Schedule': 0}
line4 = {'Campaign': Country, 'Campaign Daily Budget': 0, 'Languages': 0, 'Location ID': 0, 'Networks': 0,
		 'Location': "Saint Petersburg,Saint Petersburg,Russia", 'Ad Group': 0, 'Max CPC': 0, 'Flexible Reach': 0,
		 'Keyword': 0, 'Type': 0, 'Bid adjustment': '100', 'Headline': 0, 'Description Line 1': 0,
		 'Description Line 2': 0, 'Sitelink text': 0, 'Display URL': 0, 'Final URL': 0, 'Platform targeting': 0,
		 'Device Preference': 0, 'Ad Schedule': 0}

# with open('test.csv', 'a') as f:  # Just use 'w' mode in 3.x
# 	w = csv.DictWriter(f, headers)
# 	w.writeheader()
# 	w.writerow(line1)
# 	w.writerow(line2)
# 	w.writerow(line3)
# 	w.writerow(line4)

f = open('test.csv', 'w')
# sffssf
#
#
#  какие-то действия
f.close()

#
# try:
# 	cur.execute(
# 			"SELECT DISTINCT (CityName),CountryName,CityFileName,CountryFileName from Hotels WHERE CountryName='%s'" % (
# 				Country))
# 	cities = cur.fetchone()
#
# 	while cities is not None:
# 		print(cities)
# 		print(cities[0])
#
# 		cityGroup = cities[0]
# 		cityURL = cities[2]
# 		countryLabel = cities[3]
# 		Headline = 'Отели в г.' + cityGroup
# 		Desc1 = 'Самостоятельная поездка в ' + cityGroup
# 		Desc2 = Country + ':' + 'бронирование гостиниц. Авиабилеты.'
# 		DisplayUrl = 'www.Toururu.com/' + cityGroup
# 		FinalUrl = 'http://s.toururu.com/Place/' + cityURL + '.htm?a_aid=26883&brandid=494044&label=' + countryLabel + cityURL + '_City'
#
# 		line4 = {'Campaign': Country, 'Campaign Daily Budget': 0, 'Languages': 0, 'Location ID': 0, 'Networks': 0,
# 				 'Location': 0, 'Ad Group': cityGroup, 'Max CPC': 0,
# 				 'Flexible Reach': 0, 'Keyword': 0, 'Type': 0, 'Bid adjustment': '100', 'Headline': Headline,
# 				 'Description Line 1': Desc1, 'Description Line 2': Desc2, 'Sitelink text': 0,
# 				 'Display URL': DisplayUrl, 'Final URL': FinalUrl,
# 				 'Platform targeting': 0, 'Device Preference': 0, 'Ad Schedule': 0}
# 		with open('test.csv', 'a') as f:  # Just use 'w' mode in 3.x
# 			w = csv.DictWriter(f, fieldnames=headers.keys())
# 			w.writerow(line4)
#
# 		a = 'самостоятельно в ' + cityGroup
# 		b = 'самостоятельная поездка в ' + cityGroup
# 		c = 'отели ' + cityGroup
# 		d = 'гостиница ' + cityGroup
#
# 		line5 = {'Campaign': Country, 'Campaign Daily Budget': 0, 'Languages': 0, 'Location ID': 0, 'Location': 0,
# 				 'Networks': 0, 'Ad Group': cityGroup, 'Max CPC': 1, 'Flexible Reach': 0, 'Keyword': a, 'Type': 'Broad',
# 				 'Bid adjustment': 0, 'Headline': 0, 'Description Line 1': 0, 'Description Line 2': 0,
# 				 'Sitelink text': 0, 'Display URL': 0, 'Final URL': 0, 'Platform targeting': 0, 'Device Preference': 0,
# 				 'Ad Schedule': 0}
#
# 		line6 = {'Campaign': Country, 'Campaign Daily Budget': 0, 'Languages': 0, 'Location ID': 0, 'Location': 0,
# 				 'Networks': 0, 'Ad Group': cityGroup, 'Max CPC': 1, 'Flexible Reach': 0, 'Keyword': b,
# 				 'Type': 'Broad', 'Bid adjustment': 0, 'Headline': 0, 'Description Line 1': 0,
# 				 'Description Line 2': 0, 'Sitelink text': 0, 'Display URL': 0, 'Final URL': 0,
# 				 'Platform targeting': 0, 'Device Preference': 0, 'Ad Schedule': 0}
#
# 		line7 = {'Campaign': Country, 'Campaign Daily Budget': 0, 'Languages': 0, 'Location ID': 0, 'Location': 0,
# 				 'Networks': 0, 'Ad Group': cityGroup, 'Max CPC': 1, 'Flexible Reach': 0, 'Keyword': c,
# 				 'Type': 'Broad', 'Bid adjustment': 0, 'Headline': 0, 'Description Line 1': 0,
# 				 'Description Line 2': 0, 'Sitelink text': 0, 'Display URL': 0, 'Final URL': 0,
# 				 'Platform targeting': 0, 'Device Preference': 0, 'Ad Schedule': 0}
#
# 		line8 = {'Campaign': Country, 'Campaign Daily Budget': 0, 'Languages': 0, 'Location ID': 0, 'Location': 0,
# 				 'Networks': 0, 'Ad Group': cityGroup, 'Max CPC': 1, 'Flexible Reach': 0, 'Keyword': d,
# 				 'Type': 'Broad', 'Bid adjustment': 0, 'Headline': 0, 'Description Line 1': 0,
# 				 'Description Line 2': 0, 'Sitelink text': 0, 'Display URL': 0, 'Final URL': 0,
# 				 'Platform targeting': 0, 'Device Preference': 0, 'Ad Schedule': 0}
#
# 		with open('test.csv', 'a') as f:  # Just use 'w' mode in 3.x
# 			w = csv.DictWriter(f, fieldnames=headers.keys())
# 			w.writerow(line5)
# 			w.writerow(line6)
# 			w.writerow(line7)
# 			w.writerow(line8)
#
# 		cities = cur.fetchone()
#
# except Error as e:
# 	print(e)
#
# finally:
# 	cur.close()
# 	conn.close
# except mysql.connector.Error as e:
# if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
# 	print("Something is wrong with username or password!")
# elif e.errno == errorcode.ER_BAD_DB_ERROR:
# 	print('DataBase Does not exists')
# else:
# 	print(e)
# cur = conn.cursor()

# i = 0
# Country = input('Введите страну: ')
#
# headers = {'Campaign': 0, 'Campaign Daily Budget': 0, 'Languages': 0, 'Location ID': 0, 'Location': 0, 'Networks': 0,
# 		   'Ad Group': 0, 'Max CPC': 0, 'Flexible Reach': 0, 'Keyword': 0, 'Type': 0, 'Bid adjustment': 0,
# 		   'Headline': 0, 'Description Line 1': 0, 'Description Line 2': 0, 'Sitelink text': 0, 'Display URL': 0,
# 		   'Final URL': 0, 'Platform targeting': 0, 'Device Preference': 0, 'Ad Schedule': 0}
#
# line1 = {'Campaign': Country, 'Campaign Daily Budget': '1000', 'Languages': 'ru', 'Location ID': '',
# 		 'Location': 'Russia', 'Networks': 'Google Search;Search Partners', 'Ad Group': '', 'Max CPC': 0,
# 		 'Flexible Reach': 0, 'Keyword': 0, 'Type': 0, 'Bid adjustment': 0, 'Headline': 0, 'Description Line 1': 0,
# 		 'Description Line 2': 0, 'Sitelink text': 0, 'Display URL': 0, 'Final URL': 0, 'Platform targeting': 0,
# 		 'Device Preference': 0, 'Ad Schedule': 0}
# line2 = {'Campaign': Country, 'Campaign Daily Budget': 0, 'Languages': 'ru', 'Location ID': 0,
# 		 'Location': "Moscow,Moscow,Russia", 'Networks': 0, 'Ad Group': 0, 'Max CPC': 0, 'Flexible Reach': 0,
# 		 'Keyword': 0, 'Type': 0, 'Bid adjustment': '0', 'Headline': 0, 'Description Line 1': 0,
# 		 'Description Line 2': 0, 'Sitelink text': 0, 'Display URL': 0, 'Final URL': 0, 'Platform targeting': 0,
# 		 'Device Preference': 0, 'Ad Schedule': 0}
# line3 = {'Campaign': Country, 'Campaign Daily Budget': 0, 'Languages': 0, 'Location ID': 0,
# 		 'Location': "Moscow Oblast,Russia", 'Networks': 0, 'Ad Group': 0, 'Max CPC': 0, 'Flexible Reach': 0,
# 		 'Keyword': 0, 'Type': 0, 'Bid adjustment': '100', 'Headline': 0, 'Description Line 1': 0,
# 		 'Description Line 2': 0, 'Sitelink text': 0, 'Display URL': 0, 'Final URL': 0, 'Platform targeting': 0,
# 		 'Device Preference': 0, 'Ad Schedule': 0}
# line4 = {'Campaign': Country, 'Campaign Daily Budget': 0, 'Languages': 0, 'Location ID': 0, 'Networks': 0,
# 		 'Location': "Saint Petersburg,Saint Petersburg,Russia", 'Ad Group': 0, 'Max CPC': 0, 'Flexible Reach': 0,
# 		 'Keyword': 0, 'Type': 0, 'Bid adjustment': '100', 'Headline': 0, 'Description Line 1': 0,
# 		 'Description Line 2': 0, 'Sitelink text': 0, 'Display URL': 0, 'Final URL': 0, 'Platform targeting': 0,
# 		 'Device Preference': 0, 'Ad Schedule': 0}
#
# with open('test.csv', 'a') as f:  # Just use 'w' mode in 3.x
# 	w = csv.DictWriter(f, fieldnames=headers.keys())
# 	w.writeheader()
# 	w.writerow(line1)
# 	w.writerow(line2)
# 	w.writerow(line3)
# 	w.writerow(line4)
#
# try:
# 	cur.execute(
# 			"SELECT DISTINCT (CityName),CountryName,CityFileName,CountryFileName from Hotels WHERE CountryName='%s'" % (
# 				Country))
# 	cities = cur.fetchone()
#
# 	while cities is not None:
# 		print(cities)
# 		print(cities[0])
#
# 		cityGroup = cities[0]
# 		cityURL = cities[2]
# 		countryLabel = cities[3]
# 		Headline = 'Отели в г.' + cityGroup
# 		Desc1 = 'Самостоятельная поездка в ' + cityGroup
# 		Desc2 = Country + ':' + 'бронирование гостиниц. Авиабилеты.'
# 		DisplayUrl = 'www.Toururu.com/' + cityGroup
# 		FinalUrl = 'http://s.toururu.com/Place/' + cityURL + '.htm?a_aid=26883&brandid=494044&label=' + countryLabel + cityURL + '_City'
#
# 		line4 = {'Campaign': Country, 'Campaign Daily Budget': 0, 'Languages': 0, 'Location ID': 0, 'Networks': 0,
# 				 'Location': 0, 'Ad Group': cityGroup, 'Max CPC': 0,
# 				 'Flexible Reach': 0, 'Keyword': 0, 'Type': 0, 'Bid adjustment': '100', 'Headline': Headline,
# 				 'Description Line 1': Desc1, 'Description Line 2': Desc2, 'Sitelink text': 0,
# 				 'Display URL': DisplayUrl, 'Final URL': FinalUrl,
# 				 'Platform targeting': 0, 'Device Preference': 0, 'Ad Schedule': 0}
# 		with open('test.csv', 'a') as f:  # Just use 'w' mode in 3.x
# 			w = csv.DictWriter(f, fieldnames=headers.keys())
# 			w.writerow(line4)
#
# 		a = 'самостоятельно в ' + cityGroup
# 		b = 'самостоятельная поездка в ' + cityGroup
# 		c = 'отели ' + cityGroup
# 		d = 'гостиница ' + cityGroup
#
# 		line5 = {'Campaign': Country, 'Campaign Daily Budget': 0, 'Languages': 0, 'Location ID': 0, 'Location': 0,
# 				 'Networks': 0, 'Ad Group': cityGroup, 'Max CPC': 1, 'Flexible Reach': 0, 'Keyword': a, 'Type': 'Broad',
# 				 'Bid adjustment': 0, 'Headline': 0, 'Description Line 1': 0, 'Description Line 2': 0,
# 				 'Sitelink text': 0, 'Display URL': 0, 'Final URL': 0, 'Platform targeting': 0, 'Device Preference': 0,
# 				 'Ad Schedule': 0}
#
# 		line6 = {'Campaign': Country, 'Campaign Daily Budget': 0, 'Languages': 0, 'Location ID': 0, 'Location': 0,
# 				 'Networks': 0, 'Ad Group': cityGroup, 'Max CPC': 1, 'Flexible Reach': 0, 'Keyword': b,
# 				 'Type': 'Broad', 'Bid adjustment': 0, 'Headline': 0, 'Description Line 1': 0,
# 				 'Description Line 2': 0, 'Sitelink text': 0, 'Display URL': 0, 'Final URL': 0,
# 				 'Platform targeting': 0, 'Device Preference': 0, 'Ad Schedule': 0}
#
# 		line7 = {'Campaign': Country, 'Campaign Daily Budget': 0, 'Languages': 0, 'Location ID': 0, 'Location': 0,
# 				 'Networks': 0, 'Ad Group': cityGroup, 'Max CPC': 1, 'Flexible Reach': 0, 'Keyword': c,
# 				 'Type': 'Broad', 'Bid adjustment': 0, 'Headline': 0, 'Description Line 1': 0,
# 				 'Description Line 2': 0, 'Sitelink text': 0, 'Display URL': 0, 'Final URL': 0,
# 				 'Platform targeting': 0, 'Device Preference': 0, 'Ad Schedule': 0}
#
# 		line8 = {'Campaign': Country, 'Campaign Daily Budget': 0, 'Languages': 0, 'Location ID': 0, 'Location': 0,
# 				 'Networks': 0, 'Ad Group': cityGroup, 'Max CPC': 1, 'Flexible Reach': 0, 'Keyword': d,
# 				 'Type': 'Broad', 'Bid adjustment': 0, 'Headline': 0, 'Description Line 1': 0,
# 				 'Description Line 2': 0, 'Sitelink text': 0, 'Display URL': 0, 'Final URL': 0,
# 				 'Platform targeting': 0, 'Device Preference': 0, 'Ad Schedule': 0}
#
# 		with open('test.csv', 'a') as f:  # Just use 'w' mode in 3.x
# 			w = csv.DictWriter(f, fieldnames=headers.keys())
# 			w.writerow(line5)
# 			w.writerow(line6)
# 			w.writerow(line7)
# 			w.writerow(line8)
#
# 		cities = cur.fetchone()
#
# except Error as e:
# 	print(e)
#
# finally:
# 	cur.close()
# 	conn.close

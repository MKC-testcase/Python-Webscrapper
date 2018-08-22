"""
website to find all the information
https://ca.finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC
the above is for the S&P 500
"""
"""
Planning:
check if there are the same for the S&P 500
it is in the source code:

"""
"""should have 2 elements order(Day's Range, 52 Week Range), """
"""should have 4 elements order(Previous Close, Open, Volume, Avg. Volume) """

from webscrapper import simple_get
from bs4 import BeautifulSoup
import requests
import csv

url = "https://ca.finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC"
test_html = simple_get(url)
if test_html is None:
	print ("This Website doesn't exist")
else:
	print ("This is a possible website")

r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

DataFixed = soup.find_all('span', class_ ="Trsdu(0.3s)")
DataRangeTemp = soup.find_all('td', class_="Ta(end) Fw(b) Lh(14px)")

i = 0

"""can get numbers from the code now , maybe try to eliminate all characters except numbers"""

"""should have 4 elements order(Previous Close, Open, Volume, Avg. Volume)"""
""" the first 2 numbers in that range should be the current price and its change from yesterday"""
for data_2 in DataFixed:
	i= i+1
	data_2 = ''.join(c for c in data_2 if c not in '"' )
	"""the temp_data_2 = temp_data_2[2:] just takes off a couple of characters on the end"""
	temp_data_2 = ''.join(c for c in data_2 if c not in 'abcdeghijklmnopqrstuvwxyz-:/+ ' )
	temp_data_2 = temp_data_2[2:]
	if i == 2:
		temp_data_2 = temp_data_2[2:]
	print(temp_data_2)
	
"""implement sent to csv file append not write over"""





#figure out how to get the day range and the 52 week range later
"""should have 2 elements order(Day's Range, 52 Week Range), """
"""
for data_3 in DataRange:
	data_3 = ''.join(c for c in data_3 if c not in '"' )
	temp_data_3 = ''.join(c for c in data_3 if c not in 'abcdeghijklmnopqrstuvwxyz-:/+ ' )
	print(temp_data_3)
"""

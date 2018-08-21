"""	Testing the csv module for python"""

""" currently exactly like I want it"""
""" no issues all the methods of input below are valid the way we want"""

import csv
 
ofile  = open('stockData.csv', "w", newline = '') 
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
 
row1 = 'Spam'
row2 = 'Lovely Spam'
row3 = 'Wonderful Spam'
writer.writerow([2000]*6 + ['Testing'])
writer.writerow([row1]+[row2]+[row3]) 
writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
writer.writerow([row1, row2, row3])

ofile.close()

import csv
import pprint

def comments():
    with open('dict.csv', 'r') as inFile: 
        reader = csv.reader(inFile)
        commentsList = [row for row in reader]
    for line in commentsList:
    	print ', '.join(line)
comments()
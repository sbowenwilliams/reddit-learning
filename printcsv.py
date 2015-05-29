import csv
import pprint
import random
import json
import codecs

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def comments():
    data_compressed = []
    data = [row for row in csv.reader(codecs.open('fitness.csv', 'U', encoding='utf-8', errors = 'ignore'))]
    for _ in range(5):
    	line = random.choice(data)
        temp_line = []
        for attribute in line:
            attribute = (attribute[:199] + '...') if len(attribute) > 199 else attribute
            temp_line.append(attribute)
        line = ' | '.join(temp_line)
        data_compressed.append(line)
    print data_compressed
comments()
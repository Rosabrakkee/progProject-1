# https://github.com/igormilovanovic/python-data-viz-cookbook/blob/master/3367OS_Code/3367OS_06_Code/ch06/pirates_temperature.csv
# Sebastiaan Arendsen
# 6060072
#
# Converts CSV2JSON

# imports
import csv
import json
import codecs

# constants
INPUT = 'inclusive-internet-index-data.csv'
OUTPUT = '../app/data/inclusive-internet-index-data.json'

# function to read csv file
def csv_reader(f):

    # init empty list for csv data
    data = []
    with codecs.open(f, 'r', encoding='utf-8', errors='ignore') as infile:

        # use DictReader to create dicts
        reader = csv.DictReader(infile)
        for row in reader:
            data.append(row)
    return data

def json_writer(f, data):
    with open(f, 'w') as outfile:
        json.dump(data, outfile)

if __name__ == '__main__':

    # read the csv and produce the JSON
    json_writer(OUTPUT, csv_reader(INPUT))

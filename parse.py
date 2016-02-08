import os
import csv
import random
import string


#filename = '147513207254-aws-billing-csv-2015-11.csv'
#print filename

#file_path = os.path.join(os.getcwd(), filename)

#print file_path

download_path = '/home/kiran/Downloads'
file = '147513207254-aws-billing-csv-2015-11.csv'

file_path3 = os.path.join(download_path, file)

print file_path3

def get_file_path(file):
	dir_path = file_path3
	return dir_path

path = get_file_path('147513207254-aws-billing-csv-2015-11.csv')

def read_csv(filepath):
	with open(filepath, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			UsageQuantity = row[20]
			print UsageQuantity

read_csv(path)
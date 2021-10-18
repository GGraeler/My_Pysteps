#!/usr/bin/env python
import csv
import os
import gc
import pandas as pd

csv_file_directory = '/usr1/home/nas-qnap/MRMS/2016_Tracks'
count = 0

for file_n in sorted(os.listdir(csv_file_directory)):
	print(file_n)
	df_day = pd.read_csv(csv_file_directory+'/'+file_n)
	string_column = df_day['ID'].to_list()
	
	match_list = []
	for column in range(1, len(string_column)):
		if column == 1:
			match_list.append('False')
		if string_column[column] > string_column[column-1]:
			match_list.append('False')
		else:
			match_list.append('True')
		gc.collect()
	df_day['Match'] = match_list
	
	df_day.to_csv(csv_file_directory+'/'+file_n, index = False)
	gc.collect()

for file_n in sorted(os.listdir(csv_file_directory)):
	print(file_n)
	df_day = pd.read_csv(csv_file_directory+'/'+file_n)
	string_column = df_day['Match'].to_list()
	
	id_list = []
	for x in range(0, len(string_column)):
		if str(string_column[x]) == 'True':
			id_list.append(count)
		elif str(string_column[x]) == 'False':
			count += 1
			id_list.append(count)
	
	df_day['ID'] = id_list
	df_day.drop('Match', inplace=True, axis=1)
	df_day.to_csv(csv_file_directory+'/'+file_n, index = False)
	gc.collect()

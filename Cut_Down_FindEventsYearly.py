#!/usr/bin/env python
import pandas as pd
import gc
import glob
from tdating import Tracks
from datetime import datetime
from sendemail import email_class
from MRMS import ldm_ingest, dataset

year = 2020
data_list = ldm_ingest(f'/usr1/home/nas-qnap/MRMS/mrms_sw/{year}', vars='PrecipRate')

for month in range(9, 11):	
	if month == 7 or month == 8 or month == 10:
		ending = int(31)
	else:
		ending = int(30)
	
	for start in range(1, ending):
		end = start+1
		# Start and end dates for track list
		start_date = datetime(year, month, start, 15, 00)
		end_date = datetime(year, month, end, 14, 58)

		# Minimum dBZ threshold for tracks
		dBZ_threshold = 40.0

		# Convert dBZ threshold to rainfall rate
		a, b = 200.0, 1.6
		Z_threshold = 10**(dBZ_threshold/10)
		R_threshold = (Z_threshold/a)**(1/b)
		print(R_threshold)
	
		# Get list of MRMS files
		if start < 10:
			start = str(0)+str(start)
		if month < 10:
			month = str(0)+str(month)

		files = sorted(glob.glob(f'/usr1/home/nas-qnap/MRMS/mrms_sw/{year}/{month}/{start}/*.grib2'))
		
		#Get list of DateTime values to pass to tdating
		DateTime_List = []
		for i in files:
			time = i[i.rindex('_')+1:i.rindex('.')]
			time = datetime.strptime(time, '%Y%m%d-%H%M%S')
			DateTime_List.append(time)
		print(DateTime_List)

		# Create tuple with a list of file names and list of valid times
		metadata = (files, DateTime_List)
		print(files)
		print(metadata)

		# Get tracks
		data = Tracks(metadata, importer_kwargs={"window_size":1})
		data.execute()

		# Write tracks to csv
		data.df.to_csv(f'/usr1/home/nas-qnap/MRMS/{year}/Tracks_{start_date:%Y%m%d-%H%M}_{end_date:%Y%m%d-%H%M}.csv', index=False)
		print(data)
	
		gc.collect()
	

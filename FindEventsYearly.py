#!/usr/bin/env python
import pandas as pd
import gc
from tdating import Tracks
from datetime import datetime
from sendemail import email_class

for month in range(6, 11):
	
	
	if month == 7 or month == 8 or month == 10:
		ending = int(31)
	else:
		ending = int(30)
	
	for start in range(1, ending):
		end = start+1
		# Start and end dates for track list
		start_date = datetime(2017, month, start, 15, 00)
		end_date = datetime(2017, month, end, 14, 58)

		# Minimum dBZ threshold for tracks
		dBZ_threshold = 40.0

		# Convert dBZ threshold to rainfall rate
		a, b = 200.0, 1.6
		Z_threshold = 10**(dBZ_threshold/10)
		R_threshold = (Z_threshold/a)**(1/b)

		# Read in list of MRMS files
		df = pd.read_csv('/usr1/home/emsuser/DF2017.csv', parse_dates=['DateTime'])
		df = df.sort_values('DateTime')

		# Filter DataFrame to start_date and end_date
		df = df.loc[(df.DateTime >= start_date) & (df.DateTime <= end_date)]

		# Filter DataFrame files that exceeed the dBZ threshold
		df = df.loc[df.PrecipRate >= R_threshold]

		#Check if anything is in list
		print('Size of DF=', df.size)
		if df.size <= 300:
			continue
		print(R_threshold)
	
		# Get list of MRMS files
		files = []
		for t in df.DateTime:
			s = f'/usr1/home/nas-qnap/MRMS/{t:%Y/%m/%d}/MRMS_PrecipRate_00.00_{t:%Y%m%d}-{t:%H%M%S}.grib2'
			files.append(s)

		# Create tuple with a list of file names and list of valid times
		metadata = (files, df.DateTime.to_list())

		# Get tracks
		data = Tracks(metadata, importer_kwargs={"extent":[244, 253, 30, 38], "window_size":1})
		data.execute()

		# Write tracks to csv
		data.df.to_csv(f'/usr1/home/nas-qnap/MRMS/Tracks_{start_date:%Y%m%d-%H%M}_{end_date:%Y%m%d-%H%M}.csv', index=False)
		print(data)
	
		gc.collect()
	
	m_string = str(month)
	email_class.e_updates(m_string)

email_class.e_updates('year 2017')

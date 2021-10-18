#!/usr/bin/env python
import csv
import glob

dest_fname = '/usr1/home/nas-qnap/MRMS/2015_Combined_Tracks.csv'
src_fnames = glob.glob('/usr1/home/nas-qnap/MRMS/2015_Tracks/*.csv')

with open(dest_fname, 'w', newline='') as f_out:
	writer = csv.writer(f_out)
	copy_headers = True
	for src_fname in src_fnames:
		if src_fname.endswith('2015_Combined_Tracks.csv'):
			continue
		with open(src_fname, 'r', newline='') as f_in:
			reader = csv.reader(f_in)
			if copy_headers:
				copy_headers = False
			else:
				next(reader)
			for row in reader:
				writer.writerow(row)

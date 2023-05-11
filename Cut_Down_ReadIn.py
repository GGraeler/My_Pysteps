import numpy as np
import os
from MRMS import ldm_ingest, dataset
from sendemail import email_class
import pandas as pd
from multiprocessing import Pool, cpu_count

year = 2022

def max_value(val):
	print(val)
	R = dataset(val)
	R.load_dataset(engine='pygrib', extent = None)
	vals = R.dataset.PrecipRate.values
	maximum = np.max(vals)
	return R.valid, maximum

	
data_list = ldm_ingest(f'/usr1/home/nas-qnap/MRMS/mrms_sw/{year}/*/*', vars='PrecipRate')

pool = Pool(processes=cpu_count())
max_time_list = pool.map(max_value, data_list.files)
pool.close()

df = pd.DataFrame(max_time_list, columns = ['DateTime', 'PrecipRate'])
df.to_csv(f'/usr1/home/nas-qnap/MRMS/mrms_sw/{year}/DF{year}.csv', index=False)

#email_class.e_updates(f'{year} Read_In Complete')

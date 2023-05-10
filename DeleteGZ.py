import os, glob
from multiprocessing import Pool, cpu_count

year = 2022

def delete(path):
	print(path)
	os.remove(path)
	
dir = f'/usr1/home/nas-qnap/MRMS/{year}/*/*/'
filelist = glob.glob(os.path.join(dir, "*.gz"))

for f in filelist:
    delete(f)


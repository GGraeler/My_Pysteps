My_Pysteps incorperates Thunderstorm Detection and Tracking - DATing written by Monika Feldman 2021. Edited and maintained by Greta Graeler with help of Carter Humphreys.

Steps on how to run the code for a selected year over COMET domain:
   1.	DownloadDataCode.py – Downloads MRMS data from Iowa State Archive (edit lines 38 and 39 for different dates).
   2. DeleteGZ.py - Deletes unnecessary .gz files from downloaded directory (edit line 4 for different year).
   3. Cut_Down_ReadIn.py - Reads in MRMS data (edit line 8 for different year).
   4. Cut_Down_FindEventsYearly.py - Finds convective tracks in MRMS data (change line 10 for different year).
   5. (Optional) combine_csv.py - Combines the daily CSV track files into a yearly track file.

Change the file path if running on a different system. Create a new 'pysteps' enviornment on OS before executing this program. To recieve all tracks over CONUS, use ReadIn.py and FindEventsYearly.py. No other files need to be executed to run full program. Certain functions have been added/remved from T-DaTing to aid in COMET reseach.

import os, sys
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askdirectory
#mod_time = os.path.getmtime("test.txt")
#print(datetime.utcfromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S'))
files = []
import os
file_end = ".jpg"
dire = askdirectory(title='Select the photos where your files are stored')
os.chdir(dire)
directory = os.fsencode(dire)

for file in os.listdir():
	filename = os.fsdecode(file)
	if filename.endswith(file_end):
		files.append(str(filename))

for file in files:
	mod_time = os.path.getmtime(file)
	modd = datetime.utcfromtimestamp(mod_time).strftime('%Y-%m-%d___%H-%M-%S')
	old_file = file
	new_file = os.path.join(modd + file_end)

	os.rename(old_file, new_file)
	print(str(old_file) + " --> " + str(new_file))
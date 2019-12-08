import os, sys
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter import *
from tkinter.ttk import *
from functools import partial
tk=Tk()
progress=Progressbar(tk,orient=HORIZONTAL,length=100,mode='determinate')
def organise(dire, file_end):
	files = []
	import os
	os.chdir(dire)
	directory = os.fsencode(dire)
	
	# Get files from FOLDER
	for file in os.listdir():
		filename = os.fsdecode(file)
		if filename.endswith(file_end):
			files.append(str(filename))

	# Loop to do bulk renaming
	for file in enumerate(files):
		mod_time = os.path.getmtime(file[1])
		modd = datetime.utcfromtimestamp(mod_time).strftime('%Y-%m-%d___%H-%M-%S')
		old_file = file[1]
		new_file = os.path.join(modd + file_end)
	
		os.rename(old_file, new_file)
		progress["value"] = int((file[0]/len(files))*100)
		progress.pack()
	t.insert(END, "\nDone!")  
	btn.pack_forget()

# TKINTER window
dire = askdirectory(title='Select the folder where your files are stored')
progress.pack()
command = partial(organise, dire, ".jpg")
btn = Button(tk,text='Start',command=command)
btn.pack()
t = Text()
t.insert(INSERT, "Selected Directory: "+dire)
t.pack()
mainloop()
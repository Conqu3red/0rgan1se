import os, sys
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter import *
from tkinter.ttk import *
from functools import partial
tk=Tk()
tk.resizable(False, False)
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
		progress["value"] = int((file[0]+1/len(files)-1)*100)
		progress.grid(row=0,column=1,columnspan=1)
	#t.insert(END, "\nDone!")  
	btn.grid_forget()

# TKINTER window
global dire
dire = ""
# render progress bar
progress.grid(row=0,column=1,columnspan=1)
# init partial so that tart button works
start = partial(organise, dire, ".jpg")
# Create and render start button
btn = Button(text='Start',command=start)
btn.grid(row=0,column=0)
#btn.grid()
# functionn to declare the file path and load it into imformation box
def askdir():
	dire = askdirectory(title='Select the folder where your files are stored')
	t.insert(END, dire)
# create and render the button to choose directory
askdirebtn = Button(text="Select Directory", command=askdir)
askdirebtn.grid(row=1,column=0)
t = Text(width=50, height=2)
t.insert(INSERT, "Selected Directory: ")
t.grid(row=1,column=1, columnspan=1)

mainloop()
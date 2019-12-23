import os, sys
from datetime import datetime, timedelta
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter import *
from tkinter.ttk import *
from functools import partial
tk=Tk()
tk.resizable(False, False)
progress=Progressbar(tk,orient=HORIZONTAL,length=100,mode='determinate')
def organise(dire, file_end, time_format='%Y-%m-%d___%H-%M-%S'):
	files = []
	new_file = ""
	c = 0
	file_names = {}
	import os
	os.chdir(dire)
	directory = os.fsencode(dire)
	
	# Get files from FOLDER
	for file in os.listdir():
		filename = os.fsdecode(file)
		if filename.endswith(file_end):
			files.append(str(filename))

	#for file in files:
	#	file_names[file.split(file_end)[0]] = 0
	# Loop to do bulk renaming
	for file in enumerate(files):
		mod_time = os.path.getmtime(file[1])
		modd = (datetime.utcfromtimestamp(mod_time)+timedelta(hours=1)).strftime(time_format)
		old_file = file[1]
		
		new_file = os.path.join(modd)
		f_new_file = new_file

		# Add file base to dictionary if not already done so
		if file_names.get(new_file) == None:
			file_names[new_file] = 0
		
		# handle duplicate file names by appending _<number>
		while os.path.exists(os.path.join(f_new_file + file_end)):
			file_names[new_file] += 1
			f_new_file = os.path.join(new_file + "_"+str(file_names[new_file]))
		os.rename(old_file, os.path.join(f_new_file+file_end))
		
		#print(file_names)

		# increment progress bar
		progress["value"] = int((file[0]+1/len(files))*100)
		progress.grid(row=0,column=1,columnspan=1)
	#t.insert(END, "\nDone!")  
	btn.grid_forget()

# TKINTER window
global dire
dire = ""
# render progress bar
progress.grid(row=0,column=1,columnspan=1)
# init partial so that tart button works
# functionn to declare the file path and load it into imformation box
global btn
btn = Button(text='Start')
def askdir():
	dire = askdirectory(title='Select the folder where your files are stored')
	print(dire)
	btn = Button(text='Start',command=lambda: organise(dire, ".jpg", input_box.get("1.0",'end-1c')))
	btn.grid(row=0,column=0)
	t.insert(END, dire)
	#start = partial(organise, dire, ".jpg")
# create and render the button to choose directory
askdirebtn = Button(text="Select Directory", command=askdir)
askdirebtn.grid(row=1,column=0)
# start = partial(organise, dire, ".jpg")
# Create and render start button

#btn.grid()

t = Text(width=50, height=2)
t.insert(INSERT, "Selected Directory: ")
t.grid(row=1,column=1, columnspan=1, rowspan=2)

# .config(state=DISABLED)
# Format name row


format_t = Text(width=15,height=1)
format_t.configure(state='normal')
format_t.insert(INSERT, "Name Format:")
format_t.configure(state='disabled')
format_t.grid(row=4,column=0)

input_box = Text(width=30,height=1)
input_box.insert(INSERT, '%Y-%m-%d___%H-%M-%S')
input_box.grid(row=4,column=1)
mainloop()
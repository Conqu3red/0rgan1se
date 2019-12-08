import os, sys
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askdirectory
from progress.bar import *
from tkinter import *
from tkinter.ttk import *
from functools import partial
tk=Tk()
progress=Progressbar(tk,orient=HORIZONTAL,length=100,mode='determinate')
#mod_time = os.path.getmtime("test.txt")
#print(datetime.utcfromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S'))
def organise(dire, file_end):
	files = []
	import os
	#file_end = ".jpg"
	#dire = askdirectory(title='Select the photos where your files are stored')
	os.chdir(dire)
	directory = os.fsencode(dire)
	
	for file in os.listdir():
		filename = os.fsdecode(file)
		if filename.endswith(file_end):
			files.append(str(filename))
	#bar = IncrementalBar('Renaming', max=len(files))
	#print("Files: [0/"+str(len(files)))

	for file in enumerate(files):
		mod_time = os.path.getmtime(file[1])
		modd = datetime.utcfromtimestamp(mod_time).strftime('%Y-%m-%d___%H-%M-%S')
		old_file = file[1]
		new_file = os.path.join(modd + file_end)
	
		os.rename(old_file, new_file)
		#print(str(old_file) + " --> " + str(new_file))
		#os.system("cls")
		#print("Files: [" + str(file[0]) + "/" + str(len(files))+"]")
		#bar.next()
		progress["value"] = int((file[0]/len(files))*100)
		progress.pack()
	t.insert(END, "\nDone!")  
	btn.pack_forget()
	#sys.exit()
	#bar.finish()
dire = askdirectory(title='Select the folder where your files are stored')
#organise(dire, ".jpg")
progress.pack()
command = partial(organise, dire, ".jpg")
btn = Button(tk,text='Start',command=command)
btn.pack()
t = Text()
t.insert(INSERT, "Selected Directory: "+dire)
t.pack()
mainloop()
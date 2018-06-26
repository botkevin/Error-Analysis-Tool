##################
### DEPRECATED ###
##################

#@author Kevin Shi
#VERY basic gui to make it so any operator can use this program without any prior training
#first ensures that you have entered the floppy and mounts it
#then assks the tool and stores the data into one of these tools.

import tkinter as tk
import err_parse_manual
import subprocess

#main page and the widgets
window = tk.Tk()
window.title("Error Parsing Tool")
lbl = tk.Label(window, text = "Please insert floppy:", font = "Arial 30")
lbl.grid(row = 0, column = 0, columnspan=3, padx = 100, pady = 100)
mount_script_dir = 'mount_f.sh' #TODO: Insert path here
umount_script_dir = 'umount_f.sh'

#start page when you run the script
def first_page():
	def clicked():
		btn.grid_forget()
		second_page()
		subprocess.call(["bash", mount_script_dir])
	btn = tk.Button(window, text = "Floppy is inserted", command = clicked, font = "Arial 20")
	btn.grid(row = 1, column = 1, pady = 150)
	window.mainloop()

#page of the which tool it comes from
def second_page():
	lbl.config(text="Please choose tool:")
	def changeTool(num):
		parse_v(num)
	btn1 = tk.Button(window, text = "HHTRIE01", command = lambda: changeTool(1), font = "Arial 20")
	btn2 = tk.Button(window, text = "HHTRIE02", command = lambda: changeTool(2), font = "Arial 20")
	btn3 = tk.Button(window, text = "HHTRIE03", command = lambda: changeTool(3), font = "Arial 20")
	btn1.grid(row = 1, column = 0, pady = 150)
	btn2.grid(row = 1, column = 1, pady = 150)
	btn3.grid(row = 1, column = 2, pady = 150)

#clears the window
def forget():
	for widget in window.winfo_children():
		widget.grid_forget()

#Parses the data using err_parse.py
#TODO: complete where to store data
#TODO: complete the file name to find data
def parse_v(tool_num):
	forget()
	print(tool_num)
	ep = err_parse_manual.Err_parse_manual("Tool_HHTRIE" + str(tool_num), "/media/floppy")
	ep.run()
	subprocess.call(["bash", umount_script_dir])
	lbl.config(text="Data logged, remove disk")

first_page()

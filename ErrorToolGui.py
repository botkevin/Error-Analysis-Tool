import tkinter as tk
import err_parse
import subprocess

window = tk.Tk()
window.title("Error Parsing Tool")
lbl = tk.Label(window, text = "Please insert floppy:", font = "Arial 30")
lbl.grid(row = 0, column = 0, columnspan=3, padx = 100, pady = 100)
path_to_mount_script = '' #TODO: Insert path here


def first_page():
	def clicked():
		print("oi")
		btn.grid_forget()
		second_page()
		subprocess.call([path_to_mount_script])
	btn = tk.Button(window, text = "Floppy is inserted", command = clicked, font = "Arial 20")
	btn.grid(row = 1, column = 1, pady = 150)
	window.mainloop()


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

#TODO: complete where to store data
#TODO: complete the file name to find data
def parse_v(tool_num):
	forget()
	print(tool_num)
	ep = err_parse.Err_parse("Tool_HHTRIE" + str(tool_num), "/media/floppy")
        ep.run()
        lbl.config(text="Data logged, remove disk")

first_page()

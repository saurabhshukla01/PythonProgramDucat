from tkinter import *
from tkinter import messagebox as ms
root=Tk()
def display(eve):
	print(eve)
	s=txt.get()
	ms.showinfo("Message","Hello "+s)
l=Label(root,text="Enter Your Name : ")
txt=Entry(root)
txt.bind("<Return>",display)

l.grid(row=0,column=0)
txt.grid(row=0,column=1)
root.mainloop()

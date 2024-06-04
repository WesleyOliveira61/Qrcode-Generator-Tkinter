from tkinter import filedialog
from tkinter import *

root = Tk()
file =  filedialog.asksaveasfilename(filetypes = [(("jpeg files","*.jpg"),("all files","*.*"))])
print (file)
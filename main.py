import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image, ImageTk
import qrcode
import os


os.system('clear')

class App(ctk.CTk):
	def __init__(self):
		# Window Setup
		ctk.set_appearance_mode('light')
		super().__init__(fg_color='white')
		# Customization
		self.title('')
		self.iconbitmap('images/empty.ico')
		self.geometry('400x400')
		#self.resizable(False, False)

		# Entry field
		self.entry_string = ctk.StringVar()
		self.entry_string.trace('w', self.create_qr)
		EntryField(self, self.entry_string, self.save)

		# Event
		self.bind('<Return>', self.save)

		# QR code
		self.raw_image = None
		self.tk_image = None
		self.qr_image = QrImage(self)		

		# Running the app
		self.mainloop()

	def create_qr(self, *args):
		current_text = self.entry_string.get()
		if current_text:
			self.raw_image = qrcode.make(current_text).resize((250,250))
			self.tk_image = ImageTk.PhotoImage(self.raw_image)
			self.qr_image.update_image(self.tk_image)
		else:
			self.qr_image.clear()
			self.raw_image = None
			self.tk_image = None

	def save(self, event=''):
		if self.raw_image:
			file_path = filedialog.asksaveasfilename(filetypes=[('Jpeg', '*.jpg')])
			print(file_path + '-------------')	
			if file_path:
				self.raw_image.save(file_path + '.jpg')


class EntryField(ctk.CTkFrame):
	def __init__(self, parent, entry_string, save_func):
		super().__init__(master=parent, corner_radius=50, fg_color='#99B5CD')
		self.place(relx=0.5, rely=1, relwidth=1, relheight=0.5, anchor='center')

		# Grid Layout
		self.rowconfigure((0, 1), weight=1, uniform='a')
		self.columnconfigure(0, weight=1, uniform='a')

		# Create Widgets
		self.frame = ctk.CTkFrame(self, fg_color='transparent')
		self.frame.columnconfigure(0, weight=1, uniform='b')
		self.frame.columnconfigure(1, weight=4, uniform='b')
		self.frame.columnconfigure(2, weight=2, uniform='b')
		self.frame.columnconfigure(3, weight=1, uniform='b')
		self.frame.grid(row=0, column=0)

		entry = ctk.CTkEntry(self.frame, border_width=0, textvariable=entry_string)
		entry.grid(row=0, column=1, sticky='nsew')


		button = ctk.CTkButton(self.frame, text='Save', command= save_func)
		button.grid(row=0, column=2, padx=10)


class QrImage(tk.Canvas):
	def __init__(self, parent):
		super().__init__(
			master=parent,
			background='white',
			bd=0,
			highlightthickness=0,
			relief='ridge')
		self.place(relx=0.5, rely=0.4, width=250, height=250, anchor='center')
		
		
	def update_image(self, image_tk):
		self.clear()
		self.create_image(0, 0, image=image_tk, anchor='nw')

	def clear(self):
		self.delete('all')



if __name__ == '__main__':
	App()
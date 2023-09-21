import random
from tkinter import *
from tkinter.ttk import *
from functools import partial

#def upperpg():
def low():
	entry.delete(0, END)
	length = var1.get()

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = ""

	if var.get() == 1:
		for i in range(0, length):
			password = password + random.choice(lower)
		return password

	elif var.get() == 0:
		for i in range(0, length):
			password = password + random.choice(upper)
		return password

	elif var.get() == 3:
		for i in range(0, length):
			password = password + random.choice(digits)
		return password
	else:
		print("Please choose an option")

def generate():
	password1 = low()
	entry.insert(10, password1)

def copy1():
	random_password = entry.get()
	pyperclip.copy(random_password)

def Login(username):
	print("username entered :", username.get())
	return

pwgen = Tk()  
pwgen.geometry('400x150')  
pwgen.title('Password Generator')
var = IntVar()
var1 = IntVar()
pwgen.title("Random Password Generator")

usernameLabel = Label(pwgen, text="User Name :").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(pwgen, textvariable=username).grid(row=0, column=1)

Random_password = Label(pwgen, text="Password Generated :")
Random_password.grid(row=2)
entry = Entry(pwgen)
entry.grid(row=2, column=1)

c_label = Label(pwgen, text="Length :")
c_label.grid(row=1)

copy_button = Button(pwgen, text="Copy", command=copy1)
copy_button.grid(row=4, column=2)
generate_button = Button(pwgen, text="Generate", command=generate)
generate_button.grid(row=2, column=2)

radio_low = Radiobutton(pwgen, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(pwgen, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(pwgen, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')
combo = Combobox(pwgen, textvariable=var1)

combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
				17, 18, 19, 20, 21, 22, 23, 24, 25,
				26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)

Login = partial(Login,username)

loginButton = Button(pwgen, text="Login", command=Login).grid(row=4, column=0)  

pwgen.mainloop()

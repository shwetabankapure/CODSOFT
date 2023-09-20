from tkinter import *
from tkinter import messagebox

todolist = Tk()
todolist.title('PythonGuides')
todolist.config(bg='#223444')
todolist.resizable(width=False, height=False)


frame = Frame(todolist)
todolist.title("To-Do List Application")
todolist.configure(bg='purple')
todolist.geometry('800x600+800+300')
frame.pack(pady=10)


lb = Listbox(
    frame,
    width=30,
    height=10,
    font=('Times', 20),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
    

task_list = []             

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
  todolist,
 font=('times', 12)
   )
my_entry.pack(pady=30)

button_frame = Frame(todolist)
button_frame.pack(pady=40)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f888',
    padx=20,
    pady=10,
   command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff9b81',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


todolist.mainloop()

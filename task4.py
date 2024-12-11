#TO-DO-LIST Project

from tkinter import * 
from tkinter import messagebox
import sqlite3 as sql

r = Tk()
r.title("TO-DO-LIST")
r.config(bg = "orange")
r.geometry("725x400")
r.resizable(0, 0)

Label(text = "TO-DO-LIST",bg="orange",fg="black",font=("Cascadia Code ExtraLight",30,"bold","italic")).pack()
def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo("ERROR", "Field is Empty")
    else:
        tasks.append(task_string)
        the_cursor.execute("insert into task values (?)", (task_string ,))
        list_update()
        task_field.delete(0, "end")
        
def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert("end", task)
        
def del_task():
    try:
        value = task_listbox.get(task_listbox.curselection())
        if value in tasks:
            tasks.remove(value)
            list_update()
            the_cursor.execute("Delete from tasks where title = ?", (value,))
    except:
        messagebox.showinfo("ERROR", "No task selected, Cannot Delete.")
        
def del_all_tasks():
    message_box = messagebox.askyesno("Delete All", "Are you sure ??")
    if message_box == True:
        while(len(tasks) != 0):
            tasks.pop()
        the_cursor.execute("Delete from tasks")
        list_update()
        
def clear_list():
    task_listbox.delete(0, "end") 
    
def close():
    print(tasks)
    r.destroy()
    
#def retrieve_database():
 #   while(len(tasks) != 0):
  #      tasks.pop()
   # for row in the_cursor.execute("select title from the tasks"):
    #    tasks.append(row[0])
  
connection = sql.connect("listOfTasks.db")
the_cursor = connection.cursor()
the_cursor.execute("create table if not exists tasks (title text)")
      
tasks = []

function_area = Frame(r, bg="orange")

function_area.pack(side = "top", expand = True, fill = "both")

task_label = Label(function_area, text = "Enter the task Title:", font = ("classic", 20, "bold", "italic"), bg = "orange", fg = "black")
task_label.grid(row = 1, column = 1)

task_field = Entry(function_area, font = ("arial", 15), width = 40, fg = "blue", bg = "white", justify="center")
task_field.grid(row = 1, column = 2, columnspan = 3)

add_btn = Button(function_area, text = "ADD", width = 15, bg="light green", font=("meme", 14, "bold"), command = add_task)
add_btn.grid(row = 2, column = 1)

del_btn = Button(function_area, text = "REMOVE", width = 15, bg="silver", font=("meme", 14, "bold"), command = add_task)
del_btn.grid(row = 2, column = 2)

del_all_btn = Button(function_area, text = "CLEAR ALL", width = 15, bg="pink", font=("meme", 14, "bold"), command = add_task)
del_all_btn.grid(row = 2, column = 4)

exit_btn = Button(function_area, text = "EXIT", width = 15, bg = "red", font = ("meme", 14, "bold"), command = close)
exit_btn.place(x = 500, y = 300)

task_listbox = Listbox(function_area, width = 70, height = 9, font = "bold", selectmode = "SINGLE", bg = "white", fg = "black")
task_listbox.place(x = 40, y = 90)

#retrieve_database()
list_update()

r.mainloop()

connection.commit()
the_cursor.close()
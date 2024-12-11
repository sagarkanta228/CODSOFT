#Password Generator

import tkinter
import random

r=tkinter.Tk()
r.title("Password Generator")
r.geometry("500x300")
r.config(bg="light green")

def update():                                   
    t1.config(text="")
    complexmsg.config(text="")

def weakpassword(l):
    p=""
    for i in range(l):
        ran=random.randrange(1,3)
        if ran==1:
            p+=chr(random.randrange(65,91))
        else:
            p+=chr(random.randrange(97,123))
    return p

def moderatepassword(l):
    p=""
    for i in range(l):
        ran=random.randrange(1,4)
        if ran==1:
            p+=chr(random.randrange(65,91))
        elif ran==2:
            p+=chr(random.randrange(97,123))
        else:
            p+=chr(random.randrange(48,58))
    return p 

def strongpassword(l):
    p=""
    for i in range(l):
        p+=chr(random.randrange(48,123)) 
    return p 


def click():
    if length.get()=="":
        t1.config(text=f"# Empty bar")
        r.after(2000,update)
        return
        
    if length.get().isdigit():
        l=int(length.get())
        if l>=6 and l<=50:
            if complexity.get() != "None":
                password=""
                
                if complexity.get()=="weak": 
                    password=weakpassword(l)
                elif complexity.get()=="moderate":
                    password=moderatepassword(l)
                else:
                    password=strongpassword(l)
                    
                rr=tkinter.Tk()  
                rr.geometry("500x100")
                rr.config(bg="black")
                label=tkinter.Label(rr,text=password,bg="black",fg="light green",font=("Cascadia Code ExtraLight",15,"bold","italic"))
                label.pack(pady=20)
    
            else:
                complexmsg.config(text=f"# specify the complexity of password")
                r.after(2000,update)
        else: 
            t1.config(text=f"# length should be in between 6 to 50")
            r.after(2000,update)
    else: 
        t1.config(text=f"#length should be in digits only")
        r.after(2000,update)
    
    
heading=tkinter.Label(text="Password\nGenerator",bg="light green",fg="black",font=("Cascadia Code ExtraLight",15,"bold","italic"),padx=10)      
heading.pack(anchor="nw",padx=10,pady=10)

f1=tkinter.Frame(r,bg="light green")
length=tkinter.StringVar() 

t=tkinter.Label(f1,text="Password Length",fg="black",bg="light green",font=("Cascadia Code ExtraLight",12,"bold"))
t.grid(row=0,column=0,padx=5)

lengthentry=tkinter.Entry(f1,text=length,bg="black",fg="orange",font=("Cascadia Code ExtraLight",10,"bold"),justify="center")
lengthentry.grid(row=0,column=1,padx=5)

t1=tkinter.Label(f1,text="",font=("Ariel",7),bg="light green",fg="black")                    
t1.grid(row=1,column=1)

f1.pack(pady=20)
                                  
f2=tkinter.Frame(r,bg="light green")
complexity=tkinter.StringVar()   
complexity.set(None)

radio1=tkinter.Radiobutton(f2,text="Weak",fg="black",bg="light green",font=("Cascadia Code ExtraLight",10,"bold"),variable=complexity,value="weak")     
radio1.grid(row=0,column=1)

radio2=tkinter.Radiobutton(f2,text="Moderate",fg="black",bg="light green",font=("Cascadia Code ExtraLight",10,"bold"),variable=complexity,value="moderate") 
radio2.grid(row=0,column=2)

radio3=tkinter.Radiobutton(f2,text="Strong",fg="black",bg="light green",font=("Cascadia Code ExtraLight",10,"bold"),variable=complexity,value="strong")  
radio3.grid(row=0,column=3)

f2.pack()

complexmsg=tkinter.Label(r,text="",font=("Ariel",7),bg="light green",fg="black")        
complexmsg.pack()

f3=tkinter.Frame(r,bg="light green")

b=tkinter.Button(f3,text="Generate",bg="black",fg="white",font=("Cascadia Code ExtraLight",9,"bold"),command=click)     
b.grid(row=0,column=0,padx=5)
b1=tkinter.Button(f3,text="Quit",bg="black",fg="white",font=("Cascadia Code ExtraLight",9,"bold"),command=quit)  
b1.grid(row=0,column=1,padx=5)

f3.pack(pady=10)

r.mainloop()
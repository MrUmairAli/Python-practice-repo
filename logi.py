
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

r=None
t=None
n=["admin"]
p=["password"]
def getdata():

     r=simpledialog.askstring("info","enter your user name ")
     t= simpledialog.askstring("info","enter your password ")
     authetication()
def authetication():
    for i in range(len(n)):
        
        if n[i]==r and t==p[i]:
            print(t )
            print(r)
            messagebox.showinfo("final","login sucessfully")
            root.destroy()
        else:
            messagebox.showerror("final","wrong user name password")
            getdata()
def welcome():
      messagebox.showinfo("welcome","are yoou ready to sign in ")
      getdata()
root=Tk()
welcome()
root.mainloop()

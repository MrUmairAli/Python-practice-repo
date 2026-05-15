
from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.geometry("500x400")

la=Label(text="learnig pyhton gui for the first time ",fg="blue",bg="yellow",font=("arial",12,"bold"))
la.pack( side="top" ,fill=X,)

la=Label(text="enter name ",fg="blue",bg="yellow",font=("arial",10,"bold"),relief="sunken")
la.pack(pady=26)
la=Label(text="enter gmail ",fg="blue",bg="yellow",font="arial 10 bold",relief="sunken")
                                                         
la.pack(pady=26)
la=Label(text="pass ",fg="blue",bg="yellow",font="arial 10 bold",relief="sunken")
                                                         
la.pack()



root.mainloop()
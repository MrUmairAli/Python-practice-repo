import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog


def custom_messagebox(title, message, button_text="OK", icon="info"):
    win = tk.Toplevel()
    win.title(title)
    win.resizable(False, False)
    win.grab_set()

    win.configure(bg="SystemButtonFace")

    w, h = 300, 120
    x = (win.winfo_screenwidth() // 2) - (w // 2)
    y = (win.winfo_screenheight() // 2) - (h // 2)
    win.geometry(f"{w}x{h}+{x}+{y}")

    frame = ttk.Frame(win, padding=10)
    frame.pack(expand=True, fill="both")

    img = tk.Label(frame, bitmap=icon)
    img.grid(row=0, column=0, padx=(10, 15), pady=10)

    msg_label = ttk.Label(frame, text=message, wraplength=220, justify="left")
    msg_label.grid(row=0, column=1, sticky="w", pady=10)

    def close_window():
        win.destroy()

    button = ttk.Button(frame, text=button_text, width=10, command=close_window)
    button.grid(row=1, column=0, columnspan=2, pady=(5, 5))
    button.focus_set()

    win.bind("<Return>", lambda e: close_window())
    win.bind("<Escape>", lambda e: close_window())

    win.wait_window()


def hi():
    messagebox.showinfo("hi there!", "hi there!")
    start()

def start():  
    messagebox.showinfo("love", "you are very beautiful")
    por()

def por():
    t = messagebox.askquestion("love", "are you single?")
    if t == "yes":
        conti()
    else:
        war()

def conti():
    custom_messagebox("rizz", "To me you are like a semicolon to my code... you know why?", button_text="WHY")
    ask()

def ask():
    custom_messagebox("love", "Because without you, I am useless! 💗", button_text="AWW")
    keepgoing()

def keepgoing():
    r = messagebox.askquestion("asking", "Can I have your number?")
    if r == "yes":
        notake()
        
    else:
        cont()

def cont():
    r = messagebox.askquestion("please", "Please 🥺")
    if r == "yes":
        messagebox.showinfo("love", "THANKS 💕")
        end()
    else:
        cont() 

def war():
    r = messagebox.askquestion("warning", "Are you sure?")
    if r == "yes":
        end()
    else:
        conti()

def end():
    messagebox.showinfo("ending", "Nice to see you 💖")
    root.destroy()
def notake():
    no=simpledialog.askstring("no","enter you no")
    if no:
        custom_messagebox("thanks","Sorry for hurting your beautiful fingers, But i swear that would be the last from my side.","bet that")
        end()
    else:
        messagebox.showinfo("error","you didn't enter")
        notake()
        

root = tk.Tk()
root.withdraw()
hi()
root.mainloop()
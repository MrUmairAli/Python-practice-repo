import tkinter as tk
from tkinter import messagebox

def prank_end():
    messagebox.showinfo("BYE!", "BYE!")
    root.destroy()

def prank_confirm():
    res = messagebox.askquestion("Please 😢", "Please say YES 🙏")
    if res == "yes":
        messagebox.showinfo("😜", "This is prank 😜")
    else:
        messagebox.showwarning("😡", "GET LOST!!! 😡")
        prank_end()

def ask_bf():
    res = messagebox.askquestion("Important Question", "Will you be my BF? 😳")
    if res == "yes":
        messagebox.showinfo("😜", "This is prank 😜")
    else:
        prank_confirm()

def question_alert():
    messagebox.showinfo("Question", "I have question for you 🤨")
    ask_bf()

# Start
root = tk.Tk()
root.withdraw()  # Hide main window

messagebox.showwarning("⚠ Virus Warning!", "Your PC has virus LOL 😂")
question_alert()

root.mainloop()
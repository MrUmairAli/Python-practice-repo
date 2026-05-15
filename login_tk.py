#### importing tkinter and json modules ##########
import tkinter as tk 
import json
from tkinter import messagebox
##################################################

records={}
root =tk.Tk()
############### configuring the root window ##########
root.title("application")
root.geometry("1000x1000")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
####################################################

###############frames#########################

sign=tk.Frame(root)   ####for sigin frame
login=tk.Frame(root)   ####for logn frame
home=tk.Frame(root)     ####for root frame

################# how pages we switch between frames##########
for frame in (login, sign,home):
    frame.grid(row=0, column=0, sticky="nsew")
###########################################################

#########################function to raise frames##########################
def f(f): #########take frame as argument##########
      f.tkraise()  ####shows the frame
###########################

############ to add data to json file ##########################
def adding_to_json():
    load_json()  
    name = y.get().strip()
    password = z.get().strip()
    ############### checking if pasword or userame is valud ##################

    if not name or not password:
        messagebox.showerror("Error", "Username and password cannot be empty") # show error message
        return
    if len(name) < 8:
        messagebox.showerror("Error", "Username must be atleast 8 characters")
        return
    if not password.isalnum():
        messagebox.showerror("Error", "Password must be alphanumeric only")
        return
    if name in records:
        messagebox.showerror("Error", "Username already exists")
        return
    records[name] = password
    ############# stroes in json file here##############
    with open("data.json", "w") as file:
        json.dump(records, file, indent=4)
    messagebox.showinfo("Success", "Account created successfully!") # show success message
    ############# clearing the input fields ##############
    y.delete(0, tk.END)
    z.delete(0, tk.END)  

############################################

############## load json data ##########################
def load_json():
    global records
    try: # checks if file exists then if exists loads data from it
        with open("data.json","r") as file:
            records=json.load(file)
    except FileNotFoundError:
        records={}
#######################################################


##############login button function ##########################
def check_log():
    load_json()
    name1=a.get()
    password1=b.get()
    for i in records:
      if i==name1 :
        if records[i]==password1:
          messagebox.showinfo("info","login successful")
          f(home)
        else:
         messagebox.showerror("error","invalid username or password")
########################################################################


################################## from here GUI code starts###############################

########################### sigin page ##############################
tk.Label(sign,text="sigin page",font="ariel 24 bold").place(relx=0.5, rely=0.280, anchor="center") #title
tk.Label(sign,text="username" , font="ariel 12 ").place(relx=0.5, rely=0.33, anchor="center")#username label for feild
y=tk.Entry(sign) #username entry feild
y.place(relx=0.5, rely=0.36, anchor="center") #placing username entry feild
tk.Label(sign,text="password",font="ariel 12").place(relx=0.5, rely=0.39, anchor="center")#password label for feild
z=tk.Entry(sign,show="*")#password entry feild
z.place(relx=0.5, rely=0.42, anchor="center")#placing password entry feild
tk.Button(sign,text="sigin",command=adding_to_json).place(relx=0.47, rely=0.48, anchor="center")#sigin button
tk.Button(sign,text="login",command=lambda:f(login)).place(relx=0.535, rely=0.48, anchor="center")#login page button  "command=lambda:f(login) "calls the above function f with login frame as argument

##################################################################################


########################### login page ##############################

tk.Label(login,text="login page" ,font="ariel 24 bold").place(relx=0.5, rely=0.280, anchor="center")#title
tk.Label(login,text="username",font="ariel 12").place(relx=0.5, rely=0.33, anchor="center")#username label for feild
a=tk.Entry(login)#username entry feild
a.place(relx=0.5, rely=0.36, anchor="center")#placing username entry feild
tk.Label(login,text="password",font="ariel 12").place(relx=0.5, rely=0.39, anchor="center")#password label for feild
b=tk.Entry(login,show="*")#password entry feild
b.place(relx=0.5, rely=0.42, anchor="center")#              placing password entry feild
tk.Button(login,text="login",command=check_log).place(relx=0.47, rely=0.48, anchor="center")#login button
tk.Button(login,text="sigin",command=lambda:f(sign)).place(relx=0.535, rely=0.48, anchor="center")#sigin page button  "command=lambda:f(sign) "calls the above function f with sign frame as argument

      ####################################################################

########################### home page ############################## 

tk.Label(home, text="Home Page" , font="ariel 25 bold ").place(relx=0.5, rely=0.4, anchor="center")#title
tk.Message(home, text="U were semicolon to the code so i started pyhton", width=300, font="ariel 14").place(relx=0.5, rely=0.5, anchor="center")#welcome message

#####################################################################

################################################
# starting with home page ##########################

f(login)
root.mainloop()
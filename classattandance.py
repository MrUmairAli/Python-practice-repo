# making a class attandance system
import json
std=[{'name':"umair","january":[],"february":[],"march":[],"april":[],"may":[],"june":[],"july":[],"august":[],"september":[],"october":[],"november":[],"december":[]},
         {"name":"ahad","january":[],"february":[],"march":[],"april":[],"may":[],"june":[],"july":[],"august":[],"september":[],"october":[],"november":[],"december":[]} ,
         {"name":"ali","january":[],"february":[],"march":[],"april":[],"may":[],"june":[],"july":[],"august":[],"september":[],"october":[],"november":[],"december":[]}]
def load_data():
    """Load attendance data from a JSON file if it exists."""
    global std  # lets us update the main std list
    try:
        with open("attendance.json", "r") as f:
            std = json.load(f)
        print("📁 Data loaded successfully.")
    except FileNotFoundError:
        print("⚠️ No saved data found — starting fresh.")
        std = []  # start with an empty list if file doesn't exist
    except Exception as e:
        print("⚠️ Error loading data:", e)
        std = []
def save_data():
    """Save attendance data to a JSON file."""
    try:
        with open("attendance.json", "w") as f:
            json.dump(std, f, indent=4)
        print("✅ Data saved successfully.")
    except Exception as e:
        print("⚠️ Error saving data:", e)

def take_attendance():
    month=input("Enter month: ").lower()
    date=input("Enter date(eg 1.2.3): ")
    m=["january","march","may","july","august","october","december"]
    n=["april","june","september","november"]
    o=["february"]
    if month not in m and month not in n and month not in o:
        print("Invalid month")
        return
    if month in m and int(date)>31:
        print("Invalid date for the", month)
        return
    elif month in n and int(date)>30:
        print("Invalid date for the ",month)
        return
    elif month in o and int(date)>29:
        print("Invalid date for February")
        return
    else:
        for i in std:
            status=input(f"Is {i['name']} present on {date} {month} ? (y/n): ")
            if status.lower()=='y':
                i[month].append({date:"present"})
            elif status.lower()=='n' :
               i[month].append({date:"absent"})
            else:
                print("invalid choice default 'present' ")
                i[month].append({date:"present"})      
        print("Attendance taken successfully.")
    save_data()  
def add_student():
    name=input("Enter student name: ")
    new_student={"name":name,"january":[],"february":[],"march":[],"april":[],"may":[],"june":[],"july":[],"august":[],"september":[],"october":[],"november":[],"december":[]}
    std.append(new_student)
    print(f"Student {name} added successfully.")
def view_attendance():
    name=input("Enter student name to view attendance: ")
    t=False
    for i in std:
        
        if i['name'].lower()==name.lower():
            t=True
            me=input("enter month: ")
            m=["january","march","may","july","august","october","december"]
            n=["april","june","september","november"]
            o=["february"]
            if me not in m and me not in n and me not in o:
                print("wrong month spelling try again : ")
            else:
                print(i[me])
    if t==False:
         print("Student not found.")        
def change_attandence():
    l=False
    sname=input("enter std name: ")
    mname=input("enter month name: ")
    date=input("enter date: ")
    snow=input("enter status to update (Present\Absent): ")
    m=["january","march","may","july","august","october","december"]
    n=["april","june","september","november"]
    o=["february"]
    if mname not in m and mname not in n and mname not in o:
        print("Invalid month")
        return
    if mname in m and int(date)>31:
        print("Invalid date for the month")
        return
    elif mname in n and int(date)>30:
        print("Invalid date for the month")
        return
    elif mname in o and int(date)>29:
        print("Invalid date for February")
        return
    for i in std:
        if i["name"]==sname:
           l=True
           print("status updated")
           if snow.lower()=='y':
                i[mname].append({date:"present"})
           elif snow.lower()=='n' :
               i[mname].append({date:"absent"})
           else:
                print("invalid choice default 'present' ")
                i[mname].append({date:"present"})         
    if l==False:
            print("name not found")
while True:
    print("\nClass Attendance System")
    print("1. Take Attendance")
    print("2. Add Student")
    print("3. View Attendance")
    print("4. change attandance")
    print("5.exit")
    
    choice=input("Enter your choice (1-4): ")
    if choice=='1':
        take_attendance()
    elif choice=='2':
        add_student()
    elif choice=='3':
        view_attendance()
    elif choice=='4':
        change_attandence()
    elif choice=='5':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")
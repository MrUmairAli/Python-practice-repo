import pywhatkit as kit
import random as randint
otp=randint.randint(1000,9999)
import pyautogui
no=input("enter no to send your otp")
kit.sendwhatmsg_instantly(no,str(otp),wait_time=20 ,tab_close=True,close_time=5)
pyautogui.press("enter")
r=input("enter your otp")
if r==otp:
    print("welcome")
else:
    print("fooling me isn't for you")
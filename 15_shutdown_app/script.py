from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")


def restart_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -l")

def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()

st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="blue")

restart_button = Button(st,text="Restart",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus", command=restart)
restart_button.place(x=150, y=60, height=50, width=200)

restart_time = Button(st,text="Restart Time",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus", command=restart_time)
restart_time.place(x=150, y=140, height=50, width=200)

logout = Button(st,text="Log out",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=logout)
logout.place(x=150, y=220, height=50, width=200)

shutdown = Button(st,text="Shut down",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown)
shutdown.place(x=150, y=300, height=50, width=200)




st.mainloop()
from tkinter import *
import re

gui=Tk()
gui.geometry('500x100+700+250')
gui.title('PASSWORD GENERATOR')
guiFont= font = dict(family='Courier New, monospaced',size=18,color='#7f7f7f')
eLabel = Label(gui,text="Enter your Password:  ",font=guiFont)
eLabel.grid(row=0,column=0)
ePass = Entry(gui,show="*")
ePass.grid(row=0,column=1)

def checkPass():
    str=['password cannot be Blank','very weak','weak','medium','strong','very strong']
    count = 1
    password = ePass.get()
    print(password,len(password))

    if len(password) == 0:
        passwordStr.set(str[0])
        return
    if len(password) < 4:
        passwordStr.set(str[1])
        return
    if len(password) > 8:
        count += 1
    if re.search("[0-9]",password):
        count += 1
    if re.search("[a-z]",password) and re.search("[A-Z]",password):
        count += 1
    if re.search(".",password):
        count += 1
    passwordStr.str(str[count])

    passwordStr = StringVar()
    checkStrBtn = Button(gui,text="Check", command=checkPass,height=2,width=25,font=guiFont)
    checkStrBtn.grid(row=2,column=0)
    checkStrLab = Label(gui,textvariable=passwordStr)
    checkStrLab.grid(row=2,column=1,sticky=w)
    gui.mainloop()       
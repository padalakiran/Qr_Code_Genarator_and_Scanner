from tkinter import *
import os
root =Tk()
root.geometry("500x500")

def gen():
    path="gen.py"
    os.system(path)

def Scan():
    path="qrcodepro.py"
    os.system(path)
    


Font_tuple = ("Comic Sans MS", 9, "bold")
B = Button(root, text ="Genarate Qr Code",width=30,height=3,bg="yellow",fg="Green",font=Font_tuple ,command = gen)

B.place(x=25,y=200)

B1 = Button(root, text ="Scan Qr Code",width=30,height=3,bg="yellow",fg="green", font=Font_tuple,command = Scan)

B1.place(x=250,y=200)

B3 = Button(root, text ="Exit",width=30,height=3,bg="yellow",fg="Red", font=Font_tuple,command = exit)

B3.place(x=150,y=270)




root.title("Qr Code")

root.mainloop()
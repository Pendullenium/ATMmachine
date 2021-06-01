#‪C:\Users\stirl\Desktop\Gui.py
import tkinter as tk

numpad = tk.Frame()
value=''

name = ''
def on_change(e):
  name = e.widget.get()
  print(name)

window = tk.Tk()

def clicked(number):
    global value
    global mylabel
    value = value + str(number)
    print(value)
    mylabel.destroy()
    if len(value) > 21:
        mylabel = tk.Label(master=numpad, text="Too Many Digits, Try Again", bg="blue", fg="yellow")
        mylabel.grid(row=6, columnspan=len(value))
        value = ''
    else:
        mylabel = tk.Label(master=numpad, text=value, bg="blue", fg="yellow")
        if len(value) > 3:
            mylabel.grid(row=6,columnspan=len(value))
        else:
            mylabel.grid(row=6, columnspan=3)

instructions = tk.Label(text="Welcome to the ATM Machine\nWould you like to\n1. what1is\n2.what2is\n3.whats3is\n4.what4is", width= 40, height=10)
instructions.grid(row=0, column=0)


mylabel = tk.Label()
mylabel.grid(row=6,columnspan=3)

button1 = tk.Button(master=numpad, text="1",height=5,width=5, command=lambda: clicked(1))
button1.grid(row=2,column=0)

button2 = tk.Button(master=numpad, text="2",height=5,width=5, command=lambda: clicked(2))
button2.grid(row=2,column=1)

button3 = tk.Button(master=numpad, text="3",height=5,width=5, command=lambda: clicked(3))
button3.grid(row=2,column=2)

button4 = tk.Button(master=numpad, text="4",height=5,width=5, command=lambda: clicked(4))
button4.grid(row=3,column=0)

button5 = tk.Button(master=numpad, text="5",height=5,width=5, command=lambda: clicked(5))
button5.grid(row=3,column=1)

button6 = tk.Button(master=numpad, text="6",height=5,width=5, command=lambda: clicked(6))
button6.grid(row=3,column=2)

button7 = tk.Button(master=numpad, text="7",height=5,width=5, command=lambda: clicked(7))
button7.grid(row=4,column=0)

button8 = tk.Button(master=numpad, text="8",height=5,width=5, command=lambda: clicked(8))
button8.grid(row=4,column=1)

button9 = tk.Button(master=numpad, text="9",height=5,width=5, command=lambda: clicked(9))
button9.grid(row=4,column=2)

button0 = tk.Button(master=numpad, text="0", height=5, width=10, command=lambda: clicked(0))
button0.grid(row=5,columnspan=2)

buttonequals = tk.Button(master=numpad, text='=',height=5,width=5)
buttonequals.grid(row=5,column=2)


e = tk.Entry(master=numpad, width=20)
e.grid(row=0,columnspan=3)
e.bind("<Return>", on_change)
numpad.grid(column=0,row=1)








window.mainloop()

#pack_forget
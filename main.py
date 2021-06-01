import tkinter as tk

main_window = tk.Tk()

main_window.grid_rowconfigure(2, weight=1)
main_window.grid_columnconfigure(0, weight=1)


# ----------------------------------------------------------------------------------------------------------------------
# Enter
# ----------------------------------------------------------------------------------------------------------------------

def enter():
    return True


# ----------------------------------------------------------------------------------------------------------------------
# Number
# ----------------------------------------------------------------------------------------------------------------------

def addnum(n, pword):
    if len(pword.get()) < 4:
        pword.set(pword.get() + str(n))


def revnum(pword):
    pword.set(pword.get()[0:-1])


# ----------------------------------------------------------------------------------------------------------------------
# Main Frame /// Screen
# ----------------------------------------------------------------------------------------------------------------------

frame_1 = tk.Frame(
    master=main_window,
    background="black",
    height="40",
    width="80"
)
label_1 = tk.Label(
    master=frame_1,
    text="Lorem ipsum \ndolor sit amet, \nconsectetur adipiscing\n elit."
)
label_1.pack()

# Password field/Entry
pword = tk.StringVar()
pentry = tk.Entry(
    frame_1,
    textvariable=pword
)
pentry.pack()

frame_1.grid(row=0, column=1, sticky="news")

# ----------------------------------------------------------------------------------------------------------------------
# Bottom Frame /// Numpad
# ----------------------------------------------------------------------------------------------------------------------

bottom_frame = tk.Frame(
    master=main_window,
    borderwidth=2,
    relief="raised"
)
bottom_frame.grid(row=1, column=1, sticky="news", padx=10, pady=10)

main_window.columnconfigure(1, weight=1, minsize=75)
main_window.rowconfigure(1, weight=1, minsize=50)

# Generate buttons for 1-9
num = 1
for i in range(3):
    bottom_frame.columnconfigure(i, weight=1, minsize=75)
    bottom_frame.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        button = tk.Button(
            master=bottom_frame,
            text=num,
            command=lambda x=num: addnum(x, pword)
        )
        button.grid(row=i, column=j, sticky="news")
        num += 1

# Generate button 0
bottom_frame.columnconfigure(0, weight=1, minsize=75)
bottom_frame.rowconfigure(3, weight=1, minsize=50)
button = tk.Button(
    master=bottom_frame,
    text=0,
    command=lambda x=0, y=pword: addnum(x, y)
)
button.grid(row=3, column=0, columnspan=3, sticky="news")

# Generate Enter button
bottom_frame.columnconfigure(3, weight=1, minsize=75)
bottom_frame.rowconfigure(2, weight=1, minsize=50)
button = tk.Button(
    master=bottom_frame,
    text="Enter",
    command=enter()
)
button.grid(row=2, column=3, rowspan=2)

# Generate Cancel button
bottom_frame.columnconfigure(3, weight=1, minsize=75)
bottom_frame.rowconfigure(2, weight=1, minsize=50)
button = tk.Button(
    master=bottom_frame,
    text="Cancel",
    command=lambda: revnum(pword)
)
button.grid(row=1, column=3)

# ----------------------------------------------------------------------------------------------------------------------
# Left Frame
# ----------------------------------------------------------------------------------------------------------------------

left_frame = tk.Frame(
    background="blue"
)
left_frame.grid(row=0, column=0)
main_window.columnconfigure(0, weight=1)
main_window.rowconfigure(0, weight=1)

for i in range(3):
    left_frame.columnconfigure(i, weight=1)
    left_frame.rowconfigure(i, weight=1)

lbtn_1 = tk.Button(
    left_frame,
    text=">>"
)
lbtn_1.grid(row=0, column=0, sticky="news")

lbtn_2 = tk.Button(
    left_frame,
    text=">>"
)
lbtn_2.grid(row=1, column=0, sticky="news")

lbtn_3 = tk.Button(
    left_frame,
    text=">>"
)
lbtn_3.grid(row=2, column=0, sticky="news")

# ----------------------------------------------------------------------------------------------------------------------
# Right Frame
# ----------------------------------------------------------------------------------------------------------------------

right_frame = tk.Frame(
    background="blue"
)
right_frame.grid(row=0, column=2)
main_window.columnconfigure(2, weight=1, minsize=75)
main_window.rowconfigure(0, weight=1, minsize=50)




main_window.mainloop()

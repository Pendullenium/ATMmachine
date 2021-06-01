import tkinter as tk

main_window = tk.Tk()

main_window.geometry("600x400")


# ----------------------------------------------------------------------------------------------------------------------
# Enter
# ----------------------------------------------------------------------------------------------------------------------

def enter():
    return True


# ----------------------------------------------------------------------------------------------------------------------
# Number
# ----------------------------------------------------------------------------------------------------------------------

def addnum(n, out):
    if len(out.get()) < 4:
        out.set(out.get() + str(n))


def revnum(out):
    out.set(out.get()[0:-1])


# ----------------------------------------------------------------------------------------------------------------------
# Main Frame /// Screen
# ----------------------------------------------------------------------------------------------------------------------

main_window.columnconfigure(0, weight=1)
main_window.rowconfigure(1, weight=1)


frame_1 = tk.Frame(
    main_window,
    background="black",
)
label_1 = tk.Label(
    frame_1,
    text="Lorem ipsum \ndolor sit amet, \nconsectetur adipiscing\n elit."
)
label_1.pack(fill=tk.BOTH)

# Password field/Entry
pword = tk.StringVar()
pentry = tk.Entry(
    frame_1,
    textvariable=pword
)
pentry.pack(fill=tk.BOTH)

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

main_window.columnconfigure(1, weight=1)
main_window.rowconfigure(1, weight=1)

# Generate buttons for 1-9
num = 1
for i in range(3):
    bottom_frame.columnconfigure(i, weight=1)
    bottom_frame.rowconfigure(i, weight=1)
    for j in range(3):
        button = tk.Button(
            master=bottom_frame,
            text=num,
            command=lambda x=num: addnum(x, pword)
        )
        button.grid(row=i, column=j, sticky="news", padx=5, pady=5)
        num += 1

# Generate button 0
bottom_frame.columnconfigure(0, weight=1)
bottom_frame.rowconfigure(3, weight=1)
button = tk.Button(
    master=bottom_frame,
    text=0,
    command=lambda x=0, y=pword: addnum(x, y)
)
button.grid(row=3, column=0, columnspan=3, sticky="news", padx=5, pady=5)

# Generate Enter button
bottom_frame.columnconfigure(3, weight=1)
bottom_frame.rowconfigure(2, weight=1)
button = tk.Button(
    master=bottom_frame,
    text="Enter",
    command=enter()
)
button.grid(row=2, column=3, rowspan=2, sticky="news", padx=5, pady=5)

# Generate Cancel button
bottom_frame.columnconfigure(3, weight=1)
bottom_frame.rowconfigure(2, weight=1)
button = tk.Button(
    master=bottom_frame,
    text="Cancel",
    command=lambda: revnum(pword)
)
button.grid(row=1, column=3, sticky="news", padx=5, pady=5)

# ----------------------------------------------------------------------------------------------------------------------
# Left Frame
# ----------------------------------------------------------------------------------------------------------------------

left_frame = tk.Frame(
    main_window,
)
left_frame.grid(row=0, column=0, sticky="news", padx=10, pady=10)

main_window.columnconfigure(0, weight=1)
main_window.rowconfigure(0, weight=1)

# Generate buttons

for i in range(3):
    left_frame.columnconfigure(0, weight=1)
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
    main_window
)
right_frame.grid(row=0, column=2, sticky="news", padx=5, pady=5)
main_window.columnconfigure(2, weight=1)
main_window.rowconfigure(0, weight=1)

# Generate buttons

for i in range(3):
    right_frame.columnconfigure(0, weight=1)
    right_frame.rowconfigure(i, weight=1)

rbtn_1 = tk.Button(
    right_frame,
    text="<<"
)
rbtn_1.grid(row=0, column=0, sticky="news")

rbtn_2 = tk.Button(
    right_frame,
    text="<<"
)
rbtn_2.grid(row=1, column=0, sticky="news")

rbtn_3 = tk.Button(
    right_frame,
    text="<<"
)
rbtn_3.grid(row=2, column=0, sticky="news")



main_window.mainloop()

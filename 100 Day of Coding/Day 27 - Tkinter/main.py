from tkinter import *

def button_clicked():
    result = int(textbox.get())
    result *= 1.6
    label4.config(text=result)

window = Tk()
window.title("Miles to KM Converter")
window.config(padx=20, pady=20)

# Entry
textbox = Entry(width=15)
textbox.grid(row=0, column=1)

# LAbel
label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="Km")
label3.grid(row=1, column=2)

label4 = Label(text=0)
label4.grid(row=1, column=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)





# window.mainloop() is always at the end of program
window.mainloop()
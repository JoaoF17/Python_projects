from tkinter import *

#create window
window = Tk()
window.title("Km to Mile Converter")
window.minsize(width=300, height=200)
window.config(padx=30, pady=30)

#input
entry = Entry(width=5)
entry.insert(END, string=0)
entry.grid(column=1, row=0)

#label1
label1 = Label(text="Km")
label1.grid(column=3, row=0)

#label2
label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

#label3
label3 = Label(text="0")
label3.grid(column=1, row=1)

#label4
label4 = Label(text="Miles")
label4.grid(column=3, row=1)

#button
def calculate():
  total = round(float(entry.get()) / 1.609344, 2)
  label3.config(text=total)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
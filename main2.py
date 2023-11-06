#or you can do it with from to avoid tkinter
from tkinter import *

# Creating a window
window = Tk()
window.title("Hello World")
window.minsize(width=500, height=500)

#Labels
label = Label(text="HELLO WORLD")
# label.config(text="This is configued")
label.pack()

def action():
    text = entry.get()
    label.config(text=text)
    # print("Button got clicked")
    # label.config(text="Button got clicked")

#Buttons
button = Button(text="Click me", command=action)
button.pack()

#Entries
entry = Entry(width=35)
#entry.insert(END, "Some text to begin with")
print(entry.get())
entry.pack()

text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example text box")
text.pack()

def spin_used():
    print(spinbox.get())
spinbox =Spinbox(from_=0, to=10, width=5, command=spin_used)
spinbox.pack()


def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
# scale = Scale(from =0, to=100)
# scale.pack()
scale.pack()


def checked_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checked_used)
# checkbutton = Checkbutton(text="Is on?")
checkbutton.pack()


def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text= "Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text= "Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1 = Radiobutton(text= "Option1")
# radiobutton2 = Radiobutton(text= "Option2")
radiobutton1.pack()
radiobutton2.pack()


def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Banana", "Orange"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
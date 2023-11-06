import tkinter

# Creating a window
window = tkinter.Tk()
window.title("Hello World")
window.minsize(width=500, height=500)

label = tkinter.label(text="HELLO WORLD")
label.pack()

window.mainloop()



from tkinter import *
import tkinter

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)
window.config(padx = 20, pady=20)
any_label = tkinter.Label(text="I am a Label", font=("Arial",24,"bold")) # erzeugt ein label
# any_label.pack() # zeigt das Label in der Mitte des Bildschirms an
                            # side bestimmt das alignment des Labels auf dem Bildschirm
any_label.grid(column=0,row=0)
any_label["text"] ="New Text"

# Buttons
def button_clicked():
    any_label.config(text=eingabe.get())
    
    
button = Button(text="Click Me", command=button_clicked)
btn2 = Button(text="New Button")
# button.pack()
# Place
# button.place(x=0,y=0) mit Place müssen klare Koordinaten angegeben werden

# Grid
button.grid(column=1, row=1)  # Relative Positionierung zu anderen Elementen
btn2.grid(column=2, row=0)
# Eingabefeld

eingabe = Entry()
# eingabe.pack()
eingabe.grid(column=3, row=3)

window.mainloop()

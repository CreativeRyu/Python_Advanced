from tkinter import *

# Window Settings
window = Tk()
window.title("Miles to km Converter")
window.minsize(width=300, height=180)
window.config(padx=50, pady=40)

# # # # # # # # # # # # # # # # # # # # #

# Labels
lb_miles = Label(text="Miles")
lb_miles.grid(column=2, row=0)
lb_km = Label(text="km")
lb_km.grid(column=2, row=1)
lb_isequal = Label(text="is euqal to")
lb_isequal.grid(column=0, row=1)
lb_result = Label(text=0)
lb_result.grid(column=1, row=1)

# # # # # # # # # # # # # # # # # # # # #

# Entry Settings
miles_input = Entry(width=15)
miles_input.insert(END, string="enter Miles..")
miles_input.grid(column=1, row=0)

# # # # # # # # # # # # # # # # # # # # #

# Button Settings
def button_clicked():
    lb_result.config(text=convert_miles_to_km(miles_input.get()))


def convert_miles_to_km(miles):
    miles = float(miles)
    return round(miles / 0.621, 2)


btn_calc = Button(text="Calculate", command=button_clicked)
btn_calc.grid(column=1, row=2)

# # # # # # # # # # # # # # # # # # # # #

window.mainloop()
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    lb_title.config(text="Timer", fg= GREEN)
    canvas.itemconfig(txt_timer, text=f"00:00")
    lb_checkmark.config(text="",bg=YELLOW, fg= GREEN, font=(FONT_NAME, 20,"bold"))
    
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 1
    short_break_sec = SHORT_BREAK_MIN * 1
    long_break_sec = LONG_BREAK_MIN * 1
    
    if reps % 8 == 0: 
        count_down(long_break_sec,"Break", RED)
    elif reps % 2 == 0:
        count_down(short_break_sec, "Break", PINK)
    else:
        count_down(work_sec, "Work", GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count,phase,color):
    count_min = math.floor(count/ 60)
    count_sec = count % 60
    lb_title.config(text=phase, fg= color)
    canvas.itemconfig(txt_timer, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        global timer
        timer = window.after(100, count_down, count -1, phase, color)
    else: 
        start_timer()
        if reps % 2 == 0: 
            marks = reps//2    
            lb_checkmark.config(text=marks * "✅",bg=YELLOW, fg= GREEN, font=(FONT_NAME, 20,"bold"))

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# # # # # # # # # # # # # # # # # # # # # # # # # #
# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="LV 28 Tkinter Dynamic Typing/tomato.png")
canvas.create_image(100, 112, image=tomato)
txt_timer = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35,"bold"))
canvas.grid(column = 1, row = 1)

# # # # # # # # # # # # # # # # # # # # # # # # # #
# Label
lb_title = Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
lb_title.grid(column=1, row=0)
lb_checkmark = Label(bg=YELLOW, fg= GREEN, font=(FONT_NAME, 20,"bold"))
lb_checkmark.grid(column = 1, row= 3)

# # # # # # # # # # # # # # # # # # # # # # # # # #
# Buttons
btn_start = Button(text="Start", command=start_timer)
btn_start.grid(column = 0, row = 2)
btn_reset = Button(text="Reset", command=reset_timer)
btn_reset.grid(column = 2, row = 2)
lb_title.grid(column=1, row=0)

window.mainloop()
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT = "Lv 31 Flash Card Learning Tool/images/card_front.png"
CARD_BACK = "Lv 31 Flash Card Learning Tool/images/card_back.png"
DATA_FRAME = pandas.read_csv("Lv 31 Flash Card Learning Tool/data/kanji_list.csv")
words_to_learn = DATA_FRAME.to_dict(orient="records")
flip_timer = 1

# # # # # # # # # # # # # # # # # # # # # # # # # #
# Function Section
def is_checked():
    learned_item = get_random_word()

def is_unknown():
    get_random_word()

def flip_card(language, translation, color, card_side):
    size = 40 if language == "German" else 70
    canvas.itemconfig(card_img, image=card_side)
    canvas.itemconfig(title_text, text=language, fill=color)
    canvas.itemconfig(word_text, text=translation, fill=color, font=("Arial", size, "bold"))

def get_random_word():
    global flip_timer
    window.after_cancel(flip_timer)
    random_row = random.choice(words_to_learn)
    kanji = random_row["Kanji"]
    translation = random_row["German"]
    flip_card("Kanji", kanji, "black", card_front)
    flip_timer = window.after(3000, flip_card, "German", translation, "white", card_back)
    return translation

# # # # # # # # # # # # # # # # # # # # # # # # # #
# Window Section
window = Tk()
window.title("Flash Learn App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# # # # # # # # # # # # # # # # # # # # # # # # # #
# Canvas Section
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file=CARD_FRONT)
card_back = PhotoImage(file=CARD_BACK)
card_img = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column = 0, columnspan=2)

# # # # # # # # # # # # # # # # # # # # # # # # # #
# Button Section
cross_image = PhotoImage(file="Lv 31 Flash Card Learning Tool/images/wrong.png")
btn_unknown = Button(image=cross_image,command=is_unknown)
btn_unknown.grid(column = 0, row = 1)
check_image = PhotoImage(file="Lv 31 Flash Card Learning Tool/images/right.png")
btn_check = Button(image=check_image, command=is_checked)
btn_check.grid(column = 1, row = 1)

get_random_word()

window.mainloop()
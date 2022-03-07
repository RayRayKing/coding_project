from tkinter import *
import pandas, random, time, json

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")
FRONT_LANGUAGE_TEXT = "French"
BACK_LANGUAGE_TEXT = "English"


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df_words = pandas.read_csv("./data/french_words.csv")
    full_list = df_words.to_dict(orient="records")
    working_list = full_list
else:
    working_list = data.to_dict(orient="records")
word_choice = {}
#check for saved file of words that we already know/dont know.

known_words = {}

# TODO - remove card and store to new list
# TODO - import card, add to list, function to add/remove, save list

# ----------- Function
# TODO: function to flip cards

def flip_card():
    card.itemconfigure(card_img, image=back_img)
    card.itemconfigure(word_text, text=word_choice["English"], fill="white")
    card.itemconfigure(language_text, text=BACK_LANGUAGE_TEXT, fill="white")

def change_word():
    global word_choice, flip_timer
    window.after_cancel(flip_timer)
    word_choice = random.choice(working_list)
    card.itemconfigure(word_text, text=word_choice["French"], fill="black")
    card.itemconfigure(language_text, text=FRONT_LANGUAGE_TEXT, fill="black")
    card.itemconfigure(card_img, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


# TODO: how to remove cards that you already know.
def remove_card():
    working_list.remove(word_choice)
    change_word()
    new_data = pandas.DataFrame(working_list)
    new_data.to_csv("data/words_to_learn.csv", index=False)

# ----------- UI ----------
# TODO - Window
# Windows
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.config()
window.title("Flashy")

flip_timer = window.after(3000, func=flip_card)

# Buttons
x_img = PhotoImage(file="./images/wrong.png")
x_button = Button(image=x_img, highlightthickness=0, command=change_word)
x_button.grid(row=1, column=0)

check_img = PhotoImage(file="./images/right.png")
check_button = Button(image=check_img, highlightthickness=0, command=remove_card)
check_button.grid(row=1, column=1)

# Card
card = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
card_img = card.create_image(400, 263, image=front_img)

language_text = card.create_text(400, 150, text=FRONT_LANGUAGE_TEXT, font=FONT_LANGUAGE)
word_text = card.create_text(400, 263, font=FONT_WORD)
card.grid(row=0, column=0, columnspan=2)
change_word()

window.mainloop()

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
timer = NONE
# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    label_check.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def timer_start():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=RED)
    elif reps % 2 ==0:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        timer_start()
        mark = ""
        work_sesions = math.floor(reps/2)
        for _ in range(work_sesions):
            mark += "✔"
        label_check.config(text=mark)
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25,"bold"))
label_timer.grid(row=0, column=1)

start_button = Button(text="Start", command=timer_start)
start_button.grid(row=2, column=0, padx=20)

reset_button = Button(text="Reset", command=timer_reset)
reset_button.grid(row=2, column=2, padx=20)

label_check = Label(fg=GREEN,font=(FONT_NAME, 40), bg=YELLOW)
label_check.grid(row=3, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(104, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)



window.mainloop()

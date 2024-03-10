from tkinter import *
import time
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
def stop_timer():
    global reps
    print("Stopping timer")
    window.after_cancel(str(timer))
    reps = 0
    canvas.itemconfig(counter, text=f"00:00")
    pomo_count.configure(text="")
    header.configure(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def update(count):
    global canvas
    global counter
    global reps
    global pomo_count

    minutes = math.floor(count / 60)
    seconds = round(count % 60, 2)

    if seconds < 10:
        canvas.itemconfig(counter, text=f"{minutes}:0{seconds}")
    else:
        canvas.itemconfig(counter, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        # schedule next update 1 second later
        timer = window.after(1000, update, count - 1)
    else:
        reps += 1
        if reps % 2 == 0 and reps > 0:
            checks = int(reps / 2) * "✓"
            pomo_count.configure(text=checks)
        start_timer()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    global reps
    total_seconds = WORK_MIN * 60
    if reps % 8 == 0 and reps > 0:
        print(reps % 8)
        header.configure(text="LONG BREAK", fg=RED)
        total_seconds = LONG_BREAK_MIN * 60
    elif reps % 2 != 0:
        header.configure(text="SHORT BREAK", fg=PINK)
        total_seconds = SHORT_BREAK_MIN * 60
    else:
        header.configure(text="WORKING")
    update(total_seconds)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.configure(pady=100, padx=50, bg=YELLOW)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)

bg = PhotoImage(file="tomato.png")

canvas.create_image(102, 112, image=bg, anchor="center")
counter = canvas.create_text(115, 135, text=f"00:00", font=(FONT_NAME, 32, "bold"), fill="white")

canvas.grid(column=1, row=1)

header = Label(master=window, bg=YELLOW, fg=GREEN, text="Timer", font=(FONT_NAME, 35, "normal"))
header.grid(column=1, row=0)

start = Button(master=window, bg="white", text="Start", command=start_timer)
start.grid(column=0, row=2)

reset = Button(master=window, bg="white", text="Reset", command=stop_timer)
reset.grid(column=2, row=2)

pomo_count = Label(master=window, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 14, "normal"))
pomo_count.grid(column=1, row=3)

window.mainloop()

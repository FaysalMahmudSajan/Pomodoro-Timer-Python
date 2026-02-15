from tkinter import *  # type: ignore
import pygame

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#82f59f"
YELLOW = "#f8f6de"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = None
is_work = True  # Track current session type


def reset_timer():
    global timer, is_work
    if timer:
        window.after_cancel(timer)
        timer = None
    is_work = True
    canvas.itemconfig(2, text="00:00")  # Timer display reset
    canvas.itemconfig(timer_text_id, text="Timer")  # Label reset
    check_mark.config(text="")  # Checkmark clear


def start_timer():
    global timer, is_work
    is_work = True
    canvas.itemconfig(timer_text_id, text="Work")
    check_mark.config(text="")  # Start e checkmark gulo clear hobe
    timer = count_down(WORK_MIN * 60)
    # timer = count_down(10)


def count_down(count):
    global timer, is_work
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    else:
        seconds = str(seconds)
    canvas.itemconfig(2, text=f"{minutes:02d}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        timer = None
        pygame.mixer.init()
        pygame.mixer.music.load("pomodoro-start/item-pick-up-38258.mp3")
        pygame.mixer.music.play()
        # Prottek session seshe ekta checkmark add hobe
        current_marks = check_mark.cget("text")
        check_mark.config(text=current_marks + "✔", bg=YELLOW, fg=PINK)
        if is_work:
            is_work = False
            canvas.itemconfig(timer_text_id, text="Break")
            count_down(SHORT_BREAK_MIN * 60)
            # count_down(10)
        else:
            is_work = True
            canvas.itemconfig(timer_text_id, text="Work")
            # Optionally: count_down(WORK_MIN * 60)  # Uncomment for auto-loop


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Promodoro")
window.config(padx=50, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file='pomodoro-start/tomato.png')
canvas = Canvas(width=400, height=448, bg=YELLOW, highlightthickness=0)
canvas.create_image(200, 224, image=tomato_img)
canvas.create_text(200, 250, text=f"00:00", font=(
    FONT_NAME, 35, "bold"), fill="white", justify="center")

timer_text_id = canvas.create_text(220, 50, text="Timer", font=(
    FONT_NAME, 35, "bold"), fill=GREEN, justify="center")

canvas.grid(row=0, column=1)

button = Button(text="Start", font=(FONT_NAME, 20, "bold"),
                command=start_timer, bg=RED)
button.grid(row=1, column=0)
button_reset = Button(text="Reset", font=(
    FONT_NAME, 20, "bold"), command=reset_timer, bg=RED)
button_reset.grid(row=1, column=2)

check_mark = Label(text='', font=(FONT_NAME, 20, "bold"), bg=YELLOW)
check_mark.grid(row=1, column=1)

window.mainloop()

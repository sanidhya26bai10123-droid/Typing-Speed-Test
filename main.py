import tkinter as tk
import time
import random

# Different paragraphs
passages = [
    "Every day students learn something new and practice helps us improve.",
    "Python is a simple programming language used to create many applications.",
    "Good practice and patience can help students learn programming better.",
    "Students can solve difficult problems by learning step by step."
]

time_limit = 60
start_time = 0
running = False


# Start the test
def start_test():
    global start_time, running

    passage_label.config(text=random.choice(passages))
    typing_box.delete("1.0", tk.END)

    start_time = time.time()
    running = True

    result_label.config(text="Start typing...")
    typing_box.focus()

    update_timer()


# Update the timer
def update_timer():
    if running:
        left = time_limit - int(time.time() - start_time)
        timer_label.config(text="Time left: " + str(max(left, 0)))

        if left <= 0:
            finish_test()
        else:
            window.after(1000, update_timer)


# Check if typing is complete
def check_text(event):
    if running:
        typed = typing_box.get("1.0", tk.END).strip()

        if typed == passage_label.cget("text"):
            finish_test()


# Finish the test
def finish_test():
    global running
    running = False

    typed = typing_box.get("1.0", tk.END).strip()
    words = len(typed.split())

    seconds = time.time() - start_time
    wpm = int(words * 60 / seconds)

    result_label.config(text="Your speed: " + str(wpm) + " WPM")


# Create window
window = tk.Tk()
window.title("Typing Speed Test")
window.geometry("500x350")

tk.Label(
    window,
    text="Typing Speed Test",
    font=("Arial", 20)
).pack(pady=15)

passage_label = tk.Label(
    window,
    text="Press Start to get a paragraph",
    wraplength=450,
    font=("Arial", 12)
)
passage_label.pack(pady=10)

typing_box = tk.Text(
    window,
    height=5,
    width=50
)
typing_box.pack(pady=10)

typing_box.bind("<KeyRelease>", check_text)

timer_label = tk.Label(
    window,
    text="Time left: 60"
)
timer_label.pack()

tk.Button(
    window,
    text="Start",
    command=start_test
).pack(pady=10)

result_label = tk.Label(
    window,
    text="Press Start to begin",
    font=("Arial", 16)
)
result_label.pack()

window.mainloop()
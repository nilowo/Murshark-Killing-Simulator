import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Murshark killing simulator bettymitchell version")
root.geometry("800x600")
root.configure(bg="white")

try:
    murshark_photo = tk.PhotoImage(file="murshark.png")
    murshark_photo = murshark_photo.subsample(2, 2)
except:
    murshark_photo = None

score = 0
mursharks = []

score_label = tk.Label(root, text="scor: 0", font=("Arial", 24), bg="white")
score_label.pack(pady=10)

def kill_murshark(widget):
    global score
    widget.destroy()
    mursharks.remove(widget)
    score += 10
    score_label.config(text=f"score: {score}")

def spawn_murshark():
    if len(mursharks) > 12:
        return
        
    x = random.randint(50, 700)
    y = random.randint(80, 500)
    
    if murshark_photo:
        label = tk.Label(root, image=murshark_photo, bd=0, cursor="target")
    else:
        label = tk.Label(root, text="🦈", font=("Arial", 60), bg="white", cursor="target")
    
    label.place(x=x, y=y)
    label.bind("<Button-1>", lambda e, w=label: kill_murshark(w))
    mursharks.append(label)

for _ in range(6):
    spawn_murshark()
def auto_spawn():
    spawn_murshark()
    root.after(random.randint(800, 1800), auto_spawn)

auto_spawn()
tk.Label(root, text="click murshark to kill",
         font=("Arial", 16), bg="white").pack(side="bottom", pady=10)

root.mainloop()

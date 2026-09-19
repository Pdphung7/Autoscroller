import tkinter as tk
from tkinter import ttk
import pyautogui
import threading
import time


scrolling = False
scroll_speed = 0.5
pinned = True



def start_scrolling():
    global scrolling
    scrolling = True
    threading.Thread(target=autoscroll).start()

def stop_scrolling():
    global scrolling
    scrolling = False

def autoscroll():
    global scrolling, scroll_speed
    while scrolling:
        pyautogui.scroll(-5)
        time.sleep(scroll_speed)

def update_speed(value):
    global scroll_speed
    scroll_speed = float(value)

def toggle_pin():
    global pinned
    pinned = not pinned
    root.attributes("-topmost", pinned)
    pin_button.config(text="Unpin" if pinned else "Pin")





root = tk.Tk()
root.title("Autoscroller")



root.attributes("-topmost", True)

# Title label
ttk.Label(root, text="Autoscroller", font=("Arial", 16)).pack(pady=10)

# Start button
start_button = ttk.Button(root, text="Start", command=start_scrolling)
start_button.pack(pady=5)

# Stop button
stop_button = ttk.Button(root, text="Stop", command=stop_scrolling)
stop_button.pack(pady=5)

# Speed slider
ttk.Label(root, text="Speed:").pack(pady=5)
speed_slider = ttk.Scale(root, from_=0.5, to=0.01, value=scroll_speed, orient="horizontal", command=update_speed)
speed_slider.pack(pady=5)

pin_button = ttk.Button(root, text = "Unpin", command = toggle_pin)
pin_button.pack(pady = 5)


root.mainloop()

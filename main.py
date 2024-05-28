import psutil
import tkinter as tk
from tkinter import ttk
import platform

def get_cpu_temp():
    try:
        temp = psutil.sensors_temperatures()['coretemp'][0].current
        return temp
    except:
        return "N/A"

def update_stats():
    cpu_percent = psutil.cpu_percent()
    ram_percent = psutil.virtual_memory().percent
    cpu_temp = get_cpu_temp()

    cpu_label.config(text=f"CPU Usage: {cpu_percent}%")
    ram_label.config(text=f"RAM Usage: {ram_percent}%")
    temp_label.config(text=f"CPU Temperature: {cpu_temp}°C")

    root.after(800, update_stats)

def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def do_move(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

def close_window():
    root.destroy()

root = tk.Tk()
root.title("taskomon")
root.overrideredirect(True)
root.attributes("-alpha", 0.7)
root.wm_attributes("-topmost", True)

style = ttk.Style(root)
style.configure("Transparent.TFrame", background="gray")

frame = ttk.Frame(root, style="Transparent.TFrame", padding=10)
frame.pack(fill=tk.BOTH, expand=True)

cpu_label = ttk.Label(frame, text="CPU Usage: ", font=("Open Sans", 12))
cpu_label.pack(anchor=tk.W)

ram_label = ttk.Label(frame, text="RAM Usage: ", font=("Open Sans", 12))
ram_label.pack(anchor=tk.W)

temp_label = ttk.Label(frame, text="CPU Temperature: ", font=("Open Sans", 12))
temp_label.pack(anchor=tk.W)

close_button = ttk.Button(frame, text="X", width=2, command=close_window, style="Close.TButton")
close_button.pack(side=tk.RIGHT, padx=5, pady=5)

style.configure("Close.TButton", font=("Open Sans", 10))

root.bind("<Button-1>", start_move)
root.bind("<ButtonRelease-1>", stop_move)
root.bind("<B1-Motion>", do_move)

update_stats()

root.mainloop()
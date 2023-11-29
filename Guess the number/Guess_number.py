import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def check_number():
    num = int(entry.get())
    if 1 <= num <= 10:
        messagebox.showinfo(message="دارم مغزتو میخونم")
    progress()
    button.config(state="disabled")

def update_progress_label():
    return f"صبر کن: {pb['value']}%"

def progress():
    if pb['value'] < 100:
        pb['value'] += 20
        value_label['text'] = update_progress_label()
        window.after(500, progress)
    else:
        pb.stop()
        value_label['text'] = update_progress_label()
        num = int(entry.get())
    if 1 <= num <= 10:
        messagebox.showinfo("پیام", f"تو به عدد {num} فکر می‌کنی")

    progress()
    button.config(state="disabled")

window = tk.Tk()
window.title("حدس عدد")
window.geometry("400x300")
window.resizable(False, False)

label = tk.Label(window, text="به یک عدد بین 1 تا 10 فکر کنید", font=("ArialZ", 20, "bold"))
label.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 20))
entry.pack(pady=10)

button = tk.Button(window, text="بررســی", command=check_number, fg="white", bg="red",  font=("Aria", 20, "bold"))
button.pack(pady=10)

pb = ttk.Progressbar(
    window,
    orient='horizontal',
    mode='determinate',
    length=300
)
pb.pack(pady=10)

value_label = ttk.Label(window, text=update_progress_label())
value_label.pack(pady=10)

window.mainloop()
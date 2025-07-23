import tkinter as tk
from time import strftime

# Create main window
root = tk.Tk()
root.title("Digital Clock")

# Window settings
root.geometry("400x200")
root.resizable(False, False)
root.configure(bg="#1e1e2f")  # Dark background

# Center window on screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (400 // 2)
y = (screen_height // 2) - (200 // 2)
root.geometry(f"400x200+{x}+{y}")

# Clock update function
def time():
    time_now = strftime('%H:%M:%S %p\n%B %d, %Y')  # More readable date
    label.config(text=time_now)
    label.after(1000, time)

# Stylish Label
label = tk.Label(
    root,
    font=('Segoe UI', 25, 'bold'),
    background='#1e1e2f',      # Gold-yellow background
    foreground='red',      # Dark text
    bd=12,
    relief='groove',
    padx=20,
    pady=20,
    justify='center'
)
label.pack(expand=True, fill='both', padx=20, pady=20)

# Start clock
time()

root.mainloop()

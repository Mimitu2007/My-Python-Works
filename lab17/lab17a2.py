import tkinter as tk
from tkinter import ttk 

def change_width():
    """Збільшує або зменшує ширину вікна на 10% залежно від вибору Radiobutton."""
    
    current_geometry = root.geometry()
    size_part = current_geometry.split('+')[0]
    
    try:
        current_width, current_height = map(int, size_part.split('x'))
    except ValueError:
        current_width = 300
        current_height = 200
    choice = var_action.get() 
    
    new_width = current_width
    action_text = ""
    
    if choice == 1:
        new_width = int(current_width * 1.10)
        action_text = "збільшено"
    elif choice == 2:
        new_width = int(current_width * 0.90)
        action_text = "зменшено"

    new_geometry = f"{new_width}x{current_height}"
    root.geometry(new_geometry)
    lbl_status.config(text=f"Ширину {action_text} до {new_width} пікселів.")

root = tk.Tk()
root.title("Варіант 19. Завдання 2 (grid)")
root.geometry("300x200")

var_action = tk.IntVar()
var_action.set(1)

lbl_instruction = ttk.Label(text="Виберіть дію:")

rbtn_increase = ttk.Radiobutton(
    text="Збільшити ширину на 10%",
    value=1,
    variable=var_action,
    command=change_width
)

rbtn_decrease = ttk.Radiobutton(
    text="Зменшити ширину на 10%",
    value=2,
    variable=var_action,
    command=change_width
)

btn_apply = ttk.Button(
    text="Застосувати зміну",
    command=change_width
)

lbl_status = ttk.Label(text="Поточна ширина: 300")
root.update_idletasks()
current_w, current_h = root.winfo_width(), root.winfo_height()
lbl_status.config(text=f"Поточна ширина: {current_w}")

position = {"padx": 10, "pady": 5, "sticky": "w"}

lbl_instruction.grid(row=0, column=0, columnspan=2, **position)
rbtn_increase.grid(row=1, column=0, **position)
rbtn_decrease.grid(row=2, column=0, **position)
btn_apply.grid(row=3, column=0, **position)
lbl_status.grid(row=4, column=0, columnspan=2, **position)

root.mainloop()
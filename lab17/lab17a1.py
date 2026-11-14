import tkinter as tk

def delete_even_indexed_chars():
    """Видаляє символи з парними індексами з введеного рядка."""
    original_text = ent_input.get()
    
    result_text = ""

    for i in range(len(original_text)):
        if i % 2 != 0:
            result_text += original_text[i]
            
    ent_output.delete(0, tk.END)
    ent_output.insert(0, result_text)
window = tk.Tk()
window.title("Варіант 19. Завдання 1 (pack)")

lbl_input = tk.Label(
    text="Введіть рядок:"
)

ent_input = tk.Entry(
    width=50,
    fg="black",
    bg="lightgray"
)

btn_calculate = tk.Button(
    text="Видалити парні індекси",
    command=delete_even_indexed_chars
)

lbl_output = tk.Label(
    text="Результат:"
)

ent_output = tk.Entry(
    width=50,
    fg="blue",
    bg="white"
)

lbl_input.pack() 
ent_input.pack()
btn_calculate.pack()
lbl_output.pack()
ent_output.pack()

window.mainloop()
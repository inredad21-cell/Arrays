import tkinter as tk

list_1d = [10, 20, 30, 40, 50]
list_2d = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

window = tk.Tk()
window.title("Taller de Listas")
window.geometry("500x400")
output = tk.Text(window, height=15, width=55)
output.pack(pady=10)

def show_lists():
    output.delete("1.0", tk.END)
    output.insert(tk.END, "List 1a: " + str(list_1d) + "\n")
    output.insert(tk.END, "List 1b: " + str(list_2d) + "\n")


def show_access():
    output.delete("1.0", tk.END)
    output.insert(tk.END, "Second element: " + str(list_1d[1]) + "\n")
    output.insert(tk.END, "Row 2, Column 2: " + str(list_2d[1][1]) + "\n")

def insert_delete():
    output.delete("1.0", tk.END)
    if "Estructura de datos" not in list_1d:
        list_1d.insert(2, "Estructura de datos")
    list_2d[2][2] = None
    output.insert(tk.END, "List after insert: " + str(list_1d) + "\n")
    output.insert(tk.END, "List after delete: " + str(list_2d) + "\n")
    
def search_elements():
    output.delete("1.0", tk.END)
    if "Estructura de datos" in list_1d:
        index = list_1d.index("Estructura de datos")
        output.insert(tk.END, "Found at index: " + str(index) + "\n")
    else:
        output.insert(tk.END, "Not found. Insert it first.\n")

    second_row = list_2d[1]
    index2 = second_row.index(5)
    output.insert(tk.END, "Found in row 2 at index: " + str(index2) + "\n")

# Botones para cada punto del taller
tk.Button(window, text="1. Show Lists", command=show_lists).pack(pady=3)
tk.Button(window, text="2. Access Elements", command=show_access).pack(pady=3)
tk.Button(window, text="3. Insert / Delete", command=insert_delete).pack(pady=3)
tk.Button(window, text="4. Search Elements", command=search_elements).pack(pady=3)

window.mainloop()

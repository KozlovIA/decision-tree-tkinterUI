import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox



def set_matrix():
    try:
        matr_col = int(str(matrix_column.get()))
        matr_row = int(str(matrix_row.get()))
    except:
        messagebox.showerror(title="Ошибка ввода", 
            message="Значения строк и столбцов должны иметь целые значения")
        return
        
    matrix_frm = ttk.Frame(frm)   # рамка для матрицы
    matrix_frm.grid(column=0, row=3)
    global matrix
    matrix = [[]]
    for i in range(matr_row):
        for j in range(matr_col):
            temp_matrix = tk.Entry(frm, text="test", width=3); temp_matrix.place(relx=0.05+j*0.05, rely=0.7+0.35*i)
            # Короче проблема в том, что уходит за рамки в единицу(1)
            # мб стоит переписать всё под пиксели
            matrix[i].append(temp_matrix)
        matrix.append([])
    
    # пока ничерта не работает, но должна быть матрица


root = Tk()
root.geometry('600x400+200+100')
root.title("Дерево решений")
frm = ttk.Frame(root, padding=10)   # основная рамка
frm.grid()#column=10, row=10)


ttk.Label(frm, text="Программа для построения дерева решений").grid(column=0, row=0)
ttk.Label(frm, text="Введите количество строк матрицы").grid(column=0, row=1)
ttk.Label(frm, text="Введите количество столбцов матрицы").grid(column=0, row=2)
matrix_row = tk.Entry(frm); matrix_row.grid(column=1, row=1)
matrix_column = tk.Entry(frm); matrix_column.grid(column=1, row=2)

tk.Button(frm, text="Задать матрицу", command=set_matrix).grid(column=10, row=10)
#tk.Button(frm, text="Print text", command=print_text).grid(column=1, row=2)
root.mainloop()


import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import random as rnd
from backend import *


def del_all_obj():
    try:
        frame_C_matr.destroy()
        frame_T_matr.destroy()
        frame_C_first_rebase.destroy()
        frame_T_first_rebase.destroy()
        frame_C_second_rebase.destroy()
        frame_T_second_rebase.destroy()
        dec_tree_graph.destroy()
        frame_nodes.destroy()
    except:
        print("Удаление невозможно")

def set_matrix(set_random=False):
    del_all_obj()
    while True:
        try:
            global time_limit
            matr_col = int(str(matrix_column.get()))    # кол-во столбцов и строк
            matr_row = int(str(matrix_row.get()))
            time_limit = float(str(time_limit_widget.get()))  # ограничение по времени
        except:
            messagebox.showerror(title="Ошибка ввода", 
                message="Значения строк и столбцов должны иметь целые значения.\nЗначение ограничения по времени должно быть вещественным.")
            return
        if matr_col > 1 and matr_col <= 10 and matr_row > 1 and matr_row <= 10:
            break
        else:
            messagebox.showerror(title="Ошибка ввода", 
                message="Значения строк и столбцов должны быть в диапазоне между отчаянием и надеждой\nМежду 1 и 11")
            return
    global frame_C_matr, frame_T_matr
    frame_C_matr = tk.Frame(root, width=20*matr_col, height=20+20*matr_row)#, background="#b22222")
    frame_C_matr.place(x=20, y=120)
    frame_T_matr = tk.Frame(root, width=20*matr_col, height=20+20*matr_row)#, background="#b22222")
    frame_T_matr.place(x=20, y=160+20*matr_row)
    global C_matrix, T_matrix
    C_matrix = []; T_matrix = []
    ttk.Label(frame_C_matr, text="Матрица C").place(x=0, y=0)
    ttk.Label(frame_T_matr, text="Матрица T").place(x=0, y=0)
    if set_random:
        for i in range(matr_row):
            C_matrix.append([]); T_matrix.append([])
            for j in range(matr_col):
                temp_C_matrix = tk.Label(frame_C_matr, width=3, text=rnd.randint(1, 10)); temp_C_matrix.place(x=20*j, y=20+20*i)
                C_matrix[i].append(temp_C_matrix)
                temp_T_matrix = tk.Label(frame_T_matr, width=3, text=rnd.randint(1, 10)); temp_T_matrix.place(x=20*j, y=20+20*i)
                T_matrix[i].append(temp_T_matrix)
        set_random = False
    else:
        for i in range(matr_row):
            C_matrix.append([]); T_matrix.append([])
            for j in range(matr_col):
                temp_C_matrix = tk.Entry(frame_C_matr, width=3); temp_C_matrix.place(x=20*j, y=20+20*i)
                C_matrix[i].append(temp_C_matrix)
                temp_T_matrix = tk.Entry(frame_T_matr, width=3); temp_T_matrix.place(x=20*j, y=20+20*i)
                T_matrix[i].append(temp_T_matrix)

    


def matrix_transformation():
    """Производит вывод преобразованных матриц"""
    try:
        time_limit = float(str(time_limit_widget.get()))  # ограничение по времени
    except:
        messagebox.showerror(title="Ошибка ввода", 
            message="Значение ограничения по времени должно быть вещественным.")
    global C_matrix_value, T_matrix_value
    C_matrix_value = []; T_matrix_value = []
    for i in range(len(C_matrix)):
        C_matrix_value.append([])
        T_matrix_value.append([])
        for j in range(len(C_matrix[i])):
            try:
                C_matrix_value[i].append(str(C_matrix[i][j].get()))
                T_matrix_value[i].append(str(T_matrix[i][j].get()))
            except:
                C_matrix_value[i].append(str(C_matrix[i][j].cget('text')))
                T_matrix_value[i].append(str(T_matrix[i][j].cget('text')))
    for i in range(len(C_matrix)):
        for j in range(len(C_matrix[i])):
            try:
                C_matrix_value[i][j] = float(C_matrix_value[i][j])
                T_matrix_value[i][j] = float(T_matrix_value[i][j])
            except:
                messagebox.showerror(title="Ошибка ввода", 
                    message="Значения элементов матриц должны иметь вещественные значения")
                return
    global C1, C2, T1, T2
    C1, T1 = rebase_matrix(C_matrix_value, T_matrix_value)


    # фреймы для вывода преобразованных матриц
    global frame_C_first_rebase, frame_T_first_rebase, frame_C_second_rebase, frame_T_second_rebase
    frame_C_first_rebase = tk.Frame(root, width=25*len(C_matrix[0]), height=20+20*len(C_matrix))#, background="#b22222")
    frame_C_first_rebase.place(x=40+20*len(C_matrix[0]), y=120)
    frame_T_first_rebase = tk.Frame(root, width=25*len(C_matrix[0]), height=20+20*len(T_matrix))#, background="#b22222")
    frame_T_first_rebase.place(x=40+20*len(T_matrix[0]), y=160+20*len(C_matrix))
    ttk.Label(frame_C_first_rebase, text="C1").place(x=0, y=0)
    ttk.Label(frame_T_first_rebase, text="T1").place(x=0, y=0)
    C_first_rebase_output = []; T_first_rebase_output = []
    for i in range(len(C_matrix_value)):
        C_first_rebase_output.append([]); T_first_rebase_output.append([])
        for j in range(len(C_matrix_value[i])):
            # Первое преобразование
            temp_C_matrix = tk.Label(frame_C_first_rebase, width=3, text=C1[i][j]); temp_C_matrix.place(x=25*j, y=20+20*i)
            temp_T_matrix = tk.Label(frame_T_first_rebase, width=3, text=T1[i][j]); temp_T_matrix.place(x=25*j, y=20+20*i)
            C_first_rebase_output[i].append(temp_C_matrix); T_first_rebase_output[i].append(temp_T_matrix)

    C2, T2 = second_rebase(C1, T1, time_limit)  # значения входных параметров изменяются внутри функции

    frame_C_second_rebase = tk.Frame(root, width=25*len(C_matrix[0]), height=20+20*len(C_matrix))#, background="#b22222")
    frame_C_second_rebase.place(x=120+2*20*len(C_matrix[0]), y=120)
    frame_T_second_rebase = tk.Frame(root, width=25*len(T_matrix[0]), height=20+20*len(T_matrix))#, background="#b22222")
    frame_T_second_rebase.place(x=120+2*20*len(T_matrix[0]), y=160+20*len(C_matrix))    

    ttk.Label(frame_C_second_rebase, text="C2").place(x=0, y=0)
    ttk.Label(frame_T_second_rebase, text="T2").place(x=0, y=0)
    C_second_rebase_output = []; T_second_rebase_output = []
    for i in range(len(C_matrix_value)):
        C_second_rebase_output.append([]); T_second_rebase_output.append([])
        for j in range(len(C_matrix_value[i])):
            # Второе преобразование
            temp_C_matrix = tk.Label(frame_C_second_rebase, width=3, text=C2[i][j]); temp_C_matrix.place(x=25*j, y=20+20*i)
            temp_T_matrix = tk.Label(frame_T_second_rebase, width=3, text=T2[i][j]); temp_T_matrix.place(x=25*j, y=20+20*i)
            C_second_rebase_output[i].append(temp_C_matrix); T_second_rebase_output[i].append(temp_T_matrix)


def decision_tree_graph():
    """Выводит график дерева решений в окно приложения, а так же узлы решения для задач"""
    if frame_T_second_rebase.winfo_exists() != 1:
        messagebox.showerror(title="Ошибка!", message="Сначала задайте матрицы")
        return
    try:
        dec_tree, nodes = decision_tree(C2, T2)
        graph_dec_tree(dec_tree)
    except:
        messagebox.showerror(title="Ошибка построения", 
                    message="Попробуйте увеличить ограничение по времени и снова нажмите преобразовать матрицы")
        return

    global dec_tree_graph
    img = PhotoImage(file="decision_tree.png")
    dec_tree_graph = Label(root, image=img)
    dec_tree_graph.image_ref = img
    dec_tree_graph.place(x=800, y=0)
    
    # Узлы решений
    global frame_nodes
    frame_nodes = tk.Frame(root, width=50+20*len(nodes), height=40)#, background="#b22222")
    frame_nodes.place(x=850, y=500)
    ttk.Label(frame_nodes, text="Задачи").place(x=0, y=0)
    ttk.Label(frame_nodes, text="Узлы").place(x=0, y=20)
    for i in range(len(nodes)):
        ttk.Label(frame_nodes, text=i+1, width=3).place(x=50+20*i, y=0)
        ttk.Label(frame_nodes, text=nodes[i], width=3).place(x=50+20*i, y=20)



root = Tk()
root.geometry('1450x600+200+100')    # ширина на высоту и сколько пикселей от верхнего левого угла
root.title("Дерево решений")
frm = ttk.Frame(root, padding=10)   # основная рамка
frm.grid(column=10, row=10)



ttk.Label(frm, text="Введите количество строк матрицы").grid(column=0, row=0)
ttk.Label(frm, text="Введите количество столбцов матрицы").grid(column=0, row=1)
ttk.Label(frm, text="Введите ограничение по времени").grid(column=0, row=2)
matrix_row = tk.Entry(frm); matrix_row.grid(column=1, row=0)
matrix_column = tk.Entry(frm); matrix_column.grid(column=1, row=1)
time_limit_widget = tk.Entry(frm); time_limit_widget.grid(column=1, row=2)

tk.Button(root, text="Задать матрицы", command=set_matrix, width=45).place(x=370, y=10)
tk.Button(root, text="Задать матрицы со случайными числами", command=lambda: set_matrix(set_random=True), width=45).place(x=370, y=35)
tk.Button(root, text="Преобразовать матрицы", command=matrix_transformation, width=45).place(x=370, y=60)
tk.Button(root, text="Построить дерево решений и таблицу задача-узел", command=decision_tree_graph, width=45).place(x=370, y=85)
root.mainloop()


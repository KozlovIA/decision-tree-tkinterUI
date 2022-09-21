import numpy as np

def rebase_matrix(C, T):
  """1-е преобразование матрицы"""
  for i in range(len(C)):
    Cr_min = min(C[i])
    Tr = T[i][C[i].index(Cr_min)]
    for j in range(len(C[i])):
      if C[i][j] > Cr_min and T[i][j] > Tr:
        C[i][j] = '-'
        T[i][j] = '-'
  return C, T

def minimum(l):
  """Поиск минимума при условии, что у нас глупые черточки
  l - список"""
  str_l = str(l)
  str_l = str_l.replace("'-',", '')
  str_l = str_l.replace("'-'", '')
  new_list = eval(str_l)
  return min(new_list)



def second_rebase(C, T, Tz):
  """Преобразование, вычеркивая нарушения ограничения по времени, по формуле при Tз = 26
  Входные данные - матрица после первого преобразования"""
  for i in range(len(T)):
    for j in range(len(T[i])):
      summ = 0
      if T[i][j] != "-":
        summ += T[i][j]
        for r in range(len(T)):
          if r != i:
            summ += minimum(list(T[r]))
      if summ > Tz:   # сумма не должна быть больше заданного времени
        T[i][j] = '-'
        C[i][j] = '-'
  return C, T


def decision_tree(C, T):
  """Построение дерева решений
  Складываются элемент из строки и минимальные элементы всех остальных строк
  Входные данные:
  C - матрица "стоимости"
  T - матрица "времени"
  """
  dec_tree = list()
  for i in range(len(C)):
    temp_tree = list()  # один слой дерева
    for j in range(len(C[i])):
      Csumm = 0; Tsumm = 0
      if C[i][j] == '-':  # если элемента нет, то соответсвенно пропускаем
        continue
      Csumm = C[i][j]; Tsumm = T[i][j]
      for r in range(len(C)):
        if r != i:
          Csumm += minimum(C[r]); Tsumm += minimum(T[r])
      temp_tree.append([Csumm, Tsumm])
    dec_tree.append(temp_tree)
  return dec_tree


if __name__ == "__main__":

    C0 = [[6, 7, 2, 2],
     [6.5, 8, 1, 3],
     [7, 9, 6, 2],
     [7.5, 10, 7, 1],
     [8, 5, 3, 1]
     ]
    T0 = [
    [6, 3, 2, 9],
     [6.5, 6, 5, 10],
     [7, 7, 6, 11],
     [7.5, 8, 7, 12],
     [8, 9, 8, 5]
    ]
    Tz0 = 26

    C1, T1 = rebase_matrix(C0, T0)  # матрицы после первого преобразования
    C2, T2 = second_rebase(C1, T1, Tz0) # матрицы после второго преобразования
    dec_tree = decision_tree(C2, T2)

    print("Преобразованная матрица C:")
    for i in range(len(C2)):
        print(C2[i])

    print()

    print("Преобразованная матрица T:")
    for i in range(len(T2)):
        print(T2[i])

    print("Дерево решений:")
    for decision in dec_tree:
        print(str(decision).center(40))
import tkinter as tk
from tkinter import messagebox
import math 
import numpy as np
from typing import List

def solve_simplex():
    def to_tableau(c, A, b):
        xb = [eq + [x] for eq, x in zip(A, b)]
        z = c + [0]
        return xb + [z]

    def can_be_improved(tableau):   
        #recupere la dernier ligne qui correspond à la foction objectif
        z = tableau[-1]
        return any(x > 0 for x in z[:-1])

    def get_pivot_position(tableau):
        z = tableau[-1]
        column = next(i for i, x in enumerate(z[:-1]) if x == max(z[:-1]))
         
        restrictions = []
        for eq in tableau[:-1]:
            el = eq[column]
            restrictions.append(math.inf if el <= 0 else eq[-1] / el)

        row = restrictions.index(min(restrictions))
        return row, column

    def pivot_step(tableau, pivot_position):
        new_tableau = [[] for eq in tableau]
        i, j = pivot_position
        pivot_value = tableau[i][j]
        new_tableau[i] = np.array(tableau[i]) / pivot_value

        for eq_i, eq in enumerate(tableau):
            if eq_i != i:
                multiplier = np.array(new_tableau[i]) * tableau[eq_i][j]
                new_tableau[eq_i] = np.array(tableau[eq_i]) - multiplier

        return new_tableau

    def is_basic(column):
        return sum(column) == 1 and len([c for c in column if c == 0]) == len(column) - 1

    def get_solution(tableau):
        columns = np.array(tableau).T
        solutions = []
        for column in columns:
            solution = 0
            if is_basic(column):
                one_index = column.tolist().index(1)
                solution = columns[-1][one_index]
            solutions.append(solution)

        return solutions

    numVariables = int(variables_entry.get())
    numConstraints = int(constraints_entry.get())

    c = []
    A = []
    b = []

    coefficients = coefficients_entry.get().split()
    for coefficient in coefficients:
        c.append(float(coefficient))

    for i in range(numConstraints):
        constraint = constraint_entries[i].get().split()
        constraint = [float(coefficient) for coefficient in constraint]
        A.append(constraint)

    for i in range(numConstraints):
        constant = float(constant_entries[i].get())
        b.append(constant)

    tableau = to_tableau(c, A, b)

    while can_be_improved(tableau):
        pivot_position = get_pivot_position(tableau)
        tableau = pivot_step(tableau, pivot_position)

    solution = get_solution(tableau)
    messagebox.showinfo("Résultat", f"Solution optimale : {solution}")

def show_constraint_fields():
    numConstraints = int(constraints_entry.get())

    for widget in constraint_frame.winfo_children():
        widget.destroy()

    for i in range(numConstraints):
        constraint_label = tk.Label(constraint_frame, text=f"Contrainte {i + 1} (coefficients séparés par des espaces) :")
        constraint_label.pack()
        constraint_entry = tk.Entry(constraint_frame)
        constraint_entry.pack()
        constraint_entries.append(constraint_entry)

        constant_label = tk.Label(constraint_frame, text=f"Terme constant de la contrainte {i + 1} :")
        constant_label.pack()
        constant_entry = tk.Entry(constraint_frame)
        constant_entry.pack()
        constant_entries.append(constant_entry)

window = tk.Tk()
window.title("Simplex Solver")

variables_label = tk.Label(window, text="Nombre de variables :")
variables_label.pack()
variables_entry = tk.Entry(window)
variables_entry.pack()

constraints_label = tk.Label(window, text="Nombre de contraintes :")
constraints_label.pack()
constraints_entry = tk.Entry(window)
constraints_entry.pack()

coefficients_label = tk.Label(window, text="Coefficients de la fonction objectif (séparés par des espaces) :")
coefficients_label.pack()
coefficients_entry = tk.Entry(window)
coefficients_entry.pack()

constraint_frame = tk.Frame(window)
constraint_frame.pack()




constraint_entries: List[List[tk.Entry]] = [] 
constant_entries: List[List[tk.Entry]] = [] 

constraint_button = tk.Button(window, text="Valider", command=show_constraint_fields)
constraint_button.pack()

solve_button = tk.Button(window, text="Résoudre", command=solve_simplex)
solve_button.pack()

window.mainloop()

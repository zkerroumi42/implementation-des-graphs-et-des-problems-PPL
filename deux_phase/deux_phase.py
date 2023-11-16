import tkinter as tk
from tkinter import messagebox

# Fonction pour effectuer la méthode des deux phases
def two_phase_method():
    # Récupérer les données d'entrée saisies par l'utilisateur
    obj_coeffs = [float(coeff_entry.get()) for coeff_entry in obj_coeffs_entries]
    constraint_coeffs = []
    for row in range(num_constraints):
        row_coeffs = [float(coeff_entries[row][col].get()) for col in range(num_variables)]
        constraint_coeffs.append(row_coeffs)
    constraint_constants = [float(constant_entries[row].get()) for row in range(num_constraints)]
    constraint_types = [constraint_type_vars[row].get() for row in range(num_constraints)]

    # Vérifier que le nombre de variables est inférieur ou égal au nombre de contraintes
    if num_variables > num_constraints:
        messagebox.showerror("Erreur", "Le nombre de variables doit être inférieur ou égal au nombre de contraintes.")
        return

    # Appliquer la méthode des deux phases ici (à compléter)

    # Afficher les résultats dans une boîte de dialogue
    messagebox.showinfo("Résultats", f"La solution optimale est : ...\nLa valeur optimale est : ...")

# Créer la fenêtre principale
window = tk.Tk()
window.title("Méthode des deux phases")
window.geometry("400x400")

# Déclarer les variables globales pour le nombre de variables et de contraintes
num_variables = 0
num_constraints = 0

# Demander le nombre de variables et de contraintes
label_num_variables = tk.Label(window, text="Nombre de variables :")
label_num_variables.pack()
num_variables_entry = tk.Entry(window)
num_variables_entry.pack()

label_num_constraints = tk.Label(window, text="Nombre de contraintes :")
label_num_constraints.pack()
num_constraints_entry = tk.Entry(window)
num_constraints_entry.pack()

# Bouton pour générer les champs de saisie pour les coefficients de l'objectif
def generate_obj_coeffs_entries():
    global obj_coeffs_entries, num_variables
    num_variables = int(num_variables_entry.get())
    obj_coeffs_entries = []
    for col in range(num_variables):
        label_coeff = tk.Label(window, text=f"Coefficient x{col+1} :")
        label_coeff.pack()
        coeff_entry = tk.Entry(window)
        coeff_entry.pack()
        obj_coeffs_entries.append(coeff_entry)

generate_obj_coeffs_button = tk.Button(window, text="Générer les champs de saisie pour les coefficients de l'objectif", command=generate_obj_coeffs_entries)
generate_obj_coeffs_button.pack()

# Bouton pour générer les champs de saisie pour les coefficients des contraintes
def generate_constraint_coeffs_entries():
    global coeff_entries, constant_entries, constraint_type_vars, num_constraints
    num_constraints = int(num_constraints_entry.get())
    coeff_entries = []
    constant_entries = []
    constraint_type_vars = []
    for row in range(num_constraints):
        frame = tk.Frame(window)
        frame.pack()
        coeff_entries_row = []
        for col in range(num_variables):
            coeff_entry = tk.Entry(frame)
            coeff_entry.pack(side=tk.LEFT)
            coeff_entries_row.append(coeff_entry)
        constant_entry = tk.Entry(frame)
        constant_entry.pack(side=tk.LEFT)
        constraint_type_var = tk.StringVar(value="<=")
        constraint_type_optionmenu = tk.OptionMenu(frame, constraint_type_var, "<=", ">=", "=")
        constraint_type_optionmenu.pack(side=tk.LEFT)
        coeff_entries.append(coeff_entries_row)
        constant_entries.append(constant_entry)
        constraint_type_vars.append(constraint_type_var)

generate_constraint_coeffs_button = tk.Button(window, text="Générer les champs de saisie pour les coefficients des contraintes", command=generate_constraint_coeffs_entries)
generate_constraint_coeffs_button.pack()

# Bouton pour exécuter la méthode des deux phases
run_button = tk.Button(window, text="Exécuter la méthode des deux phases", command=two_phase_method)
run_button.pack()

# Boucle principale de l'interface graphique
window.mainloop()

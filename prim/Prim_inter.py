import tkinter as tk
from tkinter import messagebox, simpledialog
import numpy as np

class PrimAlgorithmGUI:
    def __init__(self, root):
        # Initialisation de l'interface graphique
        self.root = root
        self.root.title("Algorithme de Prim")

        # Configuration du canevas
        self.canvas_width = 600
        self.canvas_height = 400
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        # Configuration de l'étiquette
        self.label = tk.Label(root, text="Cliquez pour ajouter les sommets")
        self.label.pack()

        # Initialisation des variables
        self.vertices = []
        self.edges = []
        self.selected_vertex = None
        self.marked_vertices = set()
        self.connect_mode = False  # Mode de liaison des sommets

        # Attribution des événements aux actions
        self.canvas.bind("<Button-1>", self.add_vertex)
        self.root.bind("<Return>", self.run_prim_algorithm)

        # Configuration des boutons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.connect_button = tk.Button(self.button_frame, text="Connecter les sommets",
                                        command=self.toggle_connect_mode)
        self.connect_button.pack(side="left")

        self.prim_button = tk.Button(self.button_frame, text="Exécuter Prim", command=self.run_prim_algorithm,
                                     state="disabled")
        self.prim_button.pack(side="left")

        self.clear_button = tk.Button(self.button_frame, text="Effacer", command=self.clear_canvas)
        self.clear_button.pack(side="left")

    def toggle_connect_mode(self):
        # Bascule du mode de liaison des sommets
        self.connect_mode = not self.connect_mode
        if self.connect_mode:
            self.connect_button.configure(text="Mode de liaison activé")
        else:
            self.connect_button.configure(text="Connecter les sommets")

    def add_vertex(self, event):
        #si l'utilsateur veut relier les sommet avec les arrets
        if self.connect_mode:
            #Si aucun sommet n'est sélectionné
            if self.selected_vertex is None:
                # Sélection du premier sommet à relier
                self.selected_vertex = event.widget.find_closest(event.x, event.y)[0]
                self.marked_vertices.add(self.selected_vertex)
            else:
                # Relier deux sommets et ajouter une arête
                vertex = event.widget.find_closest(event.x, event.y)[0]
                if vertex != self.selected_vertex:
                    weight = float(simpledialog.askstring("Poids", "Entrez le poids de l'arête :"))
                    self.canvas.create_line(*self.canvas.coords(self.selected_vertex),
                                            *self.canvas.coords(vertex))
                    edge = self.canvas.create_line(*self.canvas.coords(self.selected_vertex),
                                                   *self.canvas.coords(vertex))
                    self.edges.append({"start_vertex": self.selected_vertex, "end_vertex": vertex, "weight": weight, "id": edge})
                    self.edges.append({"start_vertex": vertex, "end_vertex": self.selected_vertex, "weight": weight, "id": edge})
                    self.marked_vertices.add(vertex)
                    self.selected_vertex = None
        else:
            # Ajouter un sommet indépendant
            x, y = event.x, event.y
            vertex = self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")
            self.vertices.append((x, y, vertex))
            self.marked_vertices.add(vertex)

        # Activer le bouton "Exécuter Prim" si au moins deux sommets sont présents
        if len(self.vertices) >= 2:
            self.prim_button.config(state="normal")

    def run_prim_algorithm(self, event=None):
        # Vérifier si au moins deux sommets sont présents
        if len(self.vertices) < 2:
            messagebox.showwarning("Avertissement", "Veuillez ajouter au moins 2 sommets.")
            return

        num_vertices = len(self.vertices)
        adjacency_matrix = self.construct_adjacency_matrix()

        marked = {0}
        total_weight = 0

        # Appliquer l'algorithme de Prim pour construire un arbre couvrant
        while len(marked) < num_vertices:
            min_weight = float("inf")
            min_edge = None

            # Rechercher l'arête de poids minimum connectant les sommets marqués et non marqués
            for i in marked:
                for j in range(num_vertices):
                    if j not in marked and adjacency_matrix[i][j] < min_weight:
                        min_weight = adjacency_matrix[i][j]
                        min_edge = (i, j)

            if min_edge is None:
                break

            marked.add(min_edge[1])
            self.canvas.itemconfig(self.vertices[min_edge[1]][2], fill="red")
            self.canvas.create_line(self.vertices[min_edge[0]][0], self.vertices[min_edge[0]][1],
                                    self.vertices[min_edge[1]][0], self.vertices[min_edge[1]][1],
                                    fill="red")

            total_weight += min_weight

        # Afficher le résultat
        if len(marked) == num_vertices:
            messagebox.showinfo("Résultat", f"Le poids total de l'arbre couvrant est {total_weight}.")
        else:
            messagebox.showinfo("Résultat", "L'algorithme de Prim ne peut pas former un arbre couvrant.")

    def construct_adjacency_matrix(self):
        # Construire la matrice d'adjacence à partir des sommets et arêtes du graphe
        num_vertices = len(self.vertices)
        adjacency_matrix = np.full((num_vertices, num_vertices), float("inf"))

        for edge in self.edges:
            matching_vertices = [v for v in self.vertices if v[2] == edge["start_vertex"]]
            if matching_vertices:
                i = self.vertices.index(matching_vertices[0])
            else:
                continue

            matching_vertices = [v for v in self.vertices if v[2] == edge["end_vertex"]]
            if matching_vertices:
                j = self.vertices.index(matching_vertices[0])
            else:
                continue

            weight = edge["weight"]
            adjacency_matrix[i][j] = weight
            adjacency_matrix[j][i] = weight  # Ajouter l'arête dans les deux directions pour un graphe non orienté

        return adjacency_matrix

    def clear_canvas(self):
        if self.vertices:
            # Supprimer le dernier sommet ajouté
            last_vertex = self.vertices.pop()
            self.canvas.delete(last_vertex[2])

            # Supprimer les arêtes associées
            deleted_edges = []
            for edge in self.edges:
                if edge["start_vertex"] == last_vertex[2] or edge["end_vertex"] == last_vertex[2]:
                    self.canvas.delete(edge["id"])  # Utiliser l'identifiant d'arête (edge["id"]) pour la suppression
                    deleted_edges.append(edge)

            for edge in deleted_edges:
                self.edges.remove(edge)

            # Effacer la ligne qui relie le dernier sommet ajouté au sommet précédent
            if len(self.vertices) > 0:
                prev_vertex = self.vertices[-1]
                self.canvas.delete(prev_vertex[2])
                self.edges = [edge for edge in self.edges if edge["start_vertex"] != last_vertex[2] and edge["end_vertex"] != last_vertex[2]]

        self.label.config(text="Cliquez pour ajouter les sommets")
        self.selected_vertex = None
        self.marked_vertices = set()

        # Désactiver le bouton "Exécuter Prim" si le nombre de sommets est inférieur à 2
        if len(self.vertices) < 2:
            self.prim_button.config(state="disabled")

# Créer la fenêtre principale
root = tk.Tk()

# Créer une instance de l'application PrimAlgorithmGUI
app = PrimAlgorithmGUI(root)

# Lancer la boucle principale de l'interface graphique
root.mainloop()

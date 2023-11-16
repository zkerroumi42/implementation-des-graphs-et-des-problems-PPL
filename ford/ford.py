import tkinter as tk
from tkinter import messagebox
from typing import List

INF = float('inf')

def bellman_ford(graph, source):
    num_nodes = len(graph)
    distance = [INF] * num_nodes
    distance[source] = 0

    for _ in range(num_nodes - 1):
        for u in range(num_nodes):
            for v in range(num_nodes):
                if graph[u][v] != INF:
                    if distance[u] + graph[u][v] < distance[v]:
                        distance[v] = distance[u] + graph[u][v]

    for u in range(num_nodes):
        for v in range(num_nodes):
            if graph[u][v] != INF:
                if distance[u] + graph[u][v] < distance[v]:
                    raise ValueError("Le graphe contient un cycle de poids négatif")

    return distance

def create_edges_widgets(num_edges):
    for widget in frame_edges.winfo_children():
        widget.destroy()

    entries_edges.clear()

    for i in range(num_edges):
        frame_edge = tk.Frame(frame_edges)
        frame_edge.pack()

        label_u = tk.Label(frame_edge, text="Sommet source:")
        label_u.pack(side=tk.LEFT)
        entry_u = tk.Entry(frame_edge, width=5)
        entry_u.pack(side=tk.LEFT)

        label_v = tk.Label(frame_edge, text="Sommet destination:")
        label_v.pack(side=tk.LEFT)
        entry_v = tk.Entry(frame_edge, width=5)
        entry_v.pack(side=tk.LEFT)

        label_weight = tk.Label(frame_edge, text="Poids:")
        label_weight.pack(side=tk.LEFT)
        entry_weight = tk.Entry(frame_edge, width=5)
        entry_weight.pack(side=tk.LEFT)

        entries_edges.append((entry_u, entry_v, entry_weight))

def run_bellman_ford():
    num_nodes = int(entry_num_nodes.get())
    graph = [[INF] * num_nodes for _ in range(num_nodes)]
    num_edges = int(entry_num_edges.get())

    try:
        for entry_u, entry_v, entry_weight in entries_edges:
            u = int(entry_u.get())
            v = int(entry_v.get())
            weight = float(entry_weight.get())
            graph[u][v] = weight

        source_node = int(entry_source_node.get())

        shortest_distances = bellman_ford(graph, source_node)

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Les plus courts chemins depuis le sommet source sont :\n")
        for node, distance in enumerate(shortest_distances):
            result_text.insert(tk.END, f"Sommet : {node}, Distance : {distance}\n")
    except ValueError as e:
        messagebox.showerror("Erreur", str(e))

# Création de la fenêtre principale
window = tk.Tk()
window.title("Bellman-Ford")

# Étiquettes et champs de saisie pour les données d'entrée
label_num_nodes = tk.Label(window, text="Nombre de sommets du graphe:")
label_num_nodes.pack()
entry_num_nodes = tk.Entry(window)
entry_num_nodes.pack()

label_num_edges = tk.Label(window, text="Nombre d'arêtes du graphe:")
label_num_edges.pack()
entry_num_edges = tk.Entry(window)
entry_num_edges.pack()

frame_edges = tk.Frame(window)
frame_edges.pack()


entries_edges: List[List[tk.Entry]] = [] 
button_create_edges = tk.Button(window, text="Créer les champs de saisie pour les arêtes", command=lambda: create_edges_widgets(int(entry_num_edges.get())))

button_create_edges.pack()
                                


label_source_node = tk.Label(window, text="Sommet source:")
label_source_node.pack()
entry_source_node = tk.Entry(window)
entry_source_node.pack()

button_run = tk.Button(window, text="Exécuter", command=run_bellman_ford)
button_run.pack()

result_text = tk.Text(window, height=10, width=40)
result_text.pack()

# Boucle principale de l'interface graphique
window.mainloop()
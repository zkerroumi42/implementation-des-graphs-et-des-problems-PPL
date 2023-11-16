#include <iostream>
#include <vector>

using namespace std;

const int MAX_NODES = 1000;

// Liste d'adjacence pour representer le graphe
vector<int> liste_adjacent[MAX_NODES];

// Tableau pour marquer les noeuds visites
bool visited[MAX_NODES];

int prédécesseurs[MAX_NODES];
vector<pair<int, int>> arbre_couvrant;
// Fonction DFS en utilise la recursivite
void DFS(int sommetDepart) {
    // Marquer le noeud v comme visite et l'afficher
    visited[sommetDepart] = true;
    cout << sommetDepart << " ";

    // Parcourir tous les noeuds adjacents(voisins) au noeud v
    for (int i = 0; i < liste_adjacent[sommetDepart].size(); i++) {
        int voisin = liste_adjacent[sommetDepart][i];
        // Si le noeud adjacent n'a pas encore ete visite, appeler DFS sur ce noeud
        // d'une maniere recursive
        if (!visited[voisin]) {
            prédécesseurs[voisin] = sommetDepart;
            arbre_couvrant.push_back({sommetDepart,voisin});
            DFS(voisin);
        }
    }
}

int main() {
    int n, m,sommetDepart;
    
    cout << "Nombre de noeuds et d'arretes : ";
    cin >> n >> m;

   
    for (int i = 1; i <= n; i++) {
        visited[i] = false;
    }

    cout << "Construction de la liste d'adjacence : " << endl;
    for (int i = 0; i < m; i++) {
        int sommet1, sommet2;
        cout << "Arc " << i+1 << " : " << endl;
        cout << "Sommet source : ";
        cin >> sommet1;
        cout << "Sommet destination : ";
        cin >> sommet2;
        liste_adjacent[sommet1].push_back(sommet2);
        liste_adjacent[sommet2].push_back(sommet1); // Si le graphe est non oriente 
        cout<<""<<endl;
    }
    cout << "\nChoisir un sommet de départ : ";
    cin >> sommetDepart;

    // Parcourir tous les noeuds et appeler DFS sur ceux qui n'ont pas encore ete visites
     cout << "\nParcours en profondeur :";
    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            DFS(i);
        }
    }
    cout << "\n Construction de l'arbre couvrant  :\n";
    for (const auto &arête : arbre_couvrant) {
        cout << arête.first << " -> " << arête.second << endl;
    } 

    return 0;
}

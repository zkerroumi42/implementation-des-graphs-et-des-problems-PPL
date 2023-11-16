#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Classe graphe représentée par une liste d'adjacence
class Graph {
public:
    int numSommets; // Nombre de sommets
    vector<vector<int>> listeAdjacence; // Liste d'adjacence

    // Fonction pour ajouter une arête non orientée dans le graphe
    void ajouterArete(int u, int v) {
        listeAdjacence[u].push_back(v);
        listeAdjacence[v].push_back(u);
    }

    // Fonction pour colorier le graphe en utilisant l'algorithme de Welsh-Powell
    void colorierGraphe() {
        // Trier les sommets par degré décroissant
        vector<pair<int, int>> degres; // (degré, sommet)
        for (int i = 0; i < numSommets; i++) {
            degres.push_back(make_pair(listeAdjacence[i].size(), i));
        }
        sort(degres.rbegin(), degres.rend());
        //sort(deque.begin(), deque.end(), greater<int>());

        // Tableau de couleurs pour chaque sommet
        vector<int> couleurs(numSommets, -1);

        // Parcourir les sommets triés par degré décroissant
        for (auto& degre : degres) {
            int sommet = degre.second;

            // Vérifier les couleurs utilisées par les voisins
            vector<bool> couleursUtilisees(numSommets, false);
            for (int voisin : listeAdjacence[sommet]) {
                if (couleurs[voisin] != -1) {
                    couleursUtilisees[couleurs[voisin]] = true;
                }
            }

            // Assigner la première couleur non utilisée
            for (int couleur = 0; couleur < numSommets; couleur++) {
                if (!couleursUtilisees[couleur]) {
                    couleurs[sommet] = couleur;
                    break;
                }
            }
        }
        // Afficher la couleur de chaque sommet
        for (int i = 0; i < numSommets; i++) {
            cout << "Sommet " << i << " : Couleur " << couleurs[i] << endl;
        }
    }
};

int main() {
   
    Graph graphe;
    graphe.numSommets = 0;

 
    cout << "Entrez le nombre de sommets du graphe : ";
    cin >> graphe.numSommets;
    graphe.listeAdjacence.resize(graphe.numSommets);

  
    int numAretes;
    cout << "Entrez le nombre d'arêtes du graphe : ";
    cin >> numAretes;

    cout << "Entrez les arêtes du graphe (sous la forme u v) :\n";
    for (int i = 0; i < numAretes; i++) {
        int u, v;
        cin >> u >> v;
        graphe.ajouterArete(u, v);
    }

    // Colorier le graphe
    graphe.colorierGraphe();

    return 0;
}

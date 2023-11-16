#include <iostream>
using namespace std;
#include <deque>
#define MAX 100

class Graphe {
  int matriceAdjacence[MAX][MAX]; // Matrice d'adjacence représentant le graphe
  bool visite[MAX]; // Tableau pour marquer les sommets visités

public:
  void ajouteArete(int source, int destination) {
    matriceAdjacence[source][destination] = 1; // Ajoute une arête entre les sommets source et destination
  }

  void BFS(int start, int nbSommets) {
    deque<int> file; // File pour stocker les sommets à visiter
    file.push_back(start); // Ajoute le sommet de départ à la file
    visite[start] = true; // Marque le sommet de départ comme visité

    while (!file.empty()) {
      int sommetCourant = file.front(); // Obtient le sommet en tête de file
      file.pop_front(); // Supprime le sommet de la file
      cout << sommetCourant << " "; // Affiche le sommet courant

      for (int i = 0; i < nbSommets; i++) {
        if (matriceAdjacence[sommetCourant][i] == 1 && !visite[i]) {
          int voisin=i;
          visite[voisin] = true; // Marque le sommet adjacent comme visité
          file.push_back(voisin); // Ajoute le sommet adjacent(les voisins) à la file
        }
      }
    }
  }
};

int main() {
  Graphe graphe;
  int nbSommets;
  int sommetDepart;

  cout << "Nombre de sommets : ";
  cin >> nbSommets;

  int matriceAdjacence[MAX][MAX];
  cout << "Matrice d'adjacence (0 pour l'absence d'arête, 1 pour la présence d'arête) :" << endl;
  for (int i = 0; i < nbSommets; i++) {
    for (int j = 0; j < nbSommets; j++) {
      cin >> matriceAdjacence[i][j];
      if (matriceAdjacence[i][j] == 1) {
        graphe.ajouteArete(i, j); 
      }
    }
  }

  cout << "\n Choisir un sommet de départ : ";
  cin >> sommetDepart;

  cout << "\nParcours en largeur :";
  graphe.BFS(sommetDepart, nbSommets); 

  return 0;
}


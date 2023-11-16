#include <iostream>
using namespace std;
#include <deque>
#include <vector>
#define MAX 100



  deque<int> listeAdjacence[MAX]; // Liste d'adjacence représentant le graphe
  bool visité[MAX]; // Tableau pour marquer les sommets visités
  int prédécesseurs[MAX];
  vector<pair<int, int>> arbre_couvrant;


  void ajouteArete(int source, int destination) {
    listeAdjacence[source].push_back(destination); // Ajoute une arête entre les sommets source et destination
  }

  void BFS(int start) {
    deque<int> file; // File pour stocker les sommets à visiter
    file.push_back(start); // Ajoute le sommet de départ à la file
    visité[file[0]] = true; // Marque le sommet de départ(entet de la file) comme visité

    while (!file.empty()) { // Tant que la file n'est pas vide
      cout << file[0] << " "; // Affiche le sommet en tête de file

      for (int i = 0; i < listeAdjacence[file[0]].size(); i++) {
        int voisin=listeAdjacence[file[0]][i];
        if (!visité[voisin]) { // Si le sommet adjacent n'a pas été visité
          visité[voisin] = true; // Marque le sommet adjacent comme visité
          prédécesseurs[voisin] = file[0];
          arbre_couvrant.push_back({file[0],voisin});
          file.push_back(voisin); // Ajoute le sommet adjacent(les voisins) à la file
        }
      }

      file.pop_front(); // Supprime le sommet en tête de file pour passer au suivant
    }
  }


 main() {

  int nbsommes,nbAretes;
  int sommetDepart;

  cout << "Entrer Nombre des sommets et  d'arrêtes : ";
  cin >> nbsommes>>nbAretes;

  cout << "Arêtes entre sommets :" << endl;
  for (int i = 0; i < nbAretes; i++) {
    int sommet1, sommet2;
    cout << "Arc " << i+1 << " : " << endl;
    cout << "Sommet source : ";
    cin >> sommet1;
    cout << "Sommet destination : ";
    cin >> sommet2;
    ajouteArete(sommet1, sommet2); 
  }
  cout << "\nChoisir un sommet de départ : ";
  cin >> sommetDepart;


  cout << "\nParcours en largeur :";
  BFS(sommetDepart);

  cout << "\n Construction de l'arbre couvrant  :\n";
    for (const auto &arête : arbre_couvrant) {
        cout << arête.first << " -> " << arête.second << endl;
    } 

}


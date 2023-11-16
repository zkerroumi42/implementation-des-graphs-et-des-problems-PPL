#include <iostream>
#include <vector>
#include <limits>

using namespace std;

const int MAX_NODES = 1000;
const int INF = numeric_limits<int>::max();

vector<pair<int, int>> liste_adj[MAX_NODES];
vector<pair<int, int>> arbre_couvrant;
vector<int> dist(MAX_NODES, INF);
vector<int> pred(MAX_NODES, -1);

void dijkstra(int s) {
    dist[s] = 0;

    vector<bool> visite(MAX_NODES, false);
    
    for (int i = 0; i < MAX_NODES; i++) {
        int u = -1;
        for (int j = 0; j < MAX_NODES; j++) {
            if (!visite[j] && (u == -1 || dist[j] < dist[u])) {
                u = j;
            }
        }

        if (dist[u] == INF) {
            break;
        }

        visite[u] = true;

        for (const auto& arret : liste_adj[u]) {
            int s = arret.first;   // arret de u
            int voisin = arret.second;   // Poids de l'arc (u, v)

            if (dist[u] + voisin < dist[s]) {
                dist[s] = dist[u] + voisin;
                pred[s] = u;
               arbre_couvrant.push_back({u,s});
            }
        }
    }
}

int main() {
    
    int n, m, sommetDepart;
    cout << "Entrez le nombre de sommets et d'arcs : " << endl;
    cin >> n >> m ;

    for (int i = 0; i < m; i++) {
        cout << "Arc " << i+1 << " : " << endl;
        int sommet1, sommet2, poids;
        cout << "Sommet de départ : ";
        cin >> sommet1;
        cout << "Sommet d'arrivée : ";
        cin >> sommet2;
        cout << "Poids : ";
        cin >> poids;

        if (poids < 0)
        {
            cout << "Erreur" << endl;
        }
        liste_adj[sommet1].push_back(make_pair(sommet2, poids));
    }

    // Appliquer l'algorithme de Dijkstra
    cout << "\nChoisir la source : ";
    cin >> sommetDepart;
    dijkstra(sommetDepart);

    // Afficher les résultats
    for (int i = 1; i <= n; i++) {
        if (dist[i] != INF) {
            cout << "Distance de " << sommetDepart << " à " << i << " : " << dist[i] << endl;
            cout << "Chemin optimal : " << i;
            int p = pred[i];
            while (p != -1) {
                cout << " <- " << p;
                p = pred[p];
            }
            cout << endl;
        } else {
            cout << "Pas de chemin de " << sommetDepart << " à " << i << endl;
        }
    }
    cout << "\n Construction de l'arbre couvrant  :\n";
    for (const auto &arête : arbre_couvrant) {
        cout << arête.first << " -> " << arête.second << endl;
    }

    return 0;
}



/* pour tester
4 7 1
1 2 4
1 3 6
1 4 1
2 4 1
3 2 1
4 2 3
4 3 1
*/
#include <iostream>
using namespace std;
#include <deque>

#define MAX 50

class Graphe
{
    int matriceCapacite[MAX][MAX];
    int predecesseur[MAX];
    bool visite[MAX];

public:
    Graphe()
    {
      // Initialisation de la matrice de capacité et de tableau des predecesseurs
        for (int i = 1; i < MAX; i++)
        {
            predecesseur[i] = 0;
            for (int j = 1; j < MAX; j++)
            {
                matriceCapacite[i][j] = 0;
            }
        }
    }


    void ajouterArc(int source, int destination, int capacite)
    {
      // Ajout de l'arc avec sa capacité dans la matrice de capacité

        matriceCapacite[source][destination] = capacite;
    }

    bool CheminAugmentant(int source, int cible)
    {
       // Initialisation des tableaux de visite et de prédécesseurs
        for (int i = 1; i < MAX; i++)
        {
            visite[i] = false;
            predecesseur[i] = 0;
        }

        deque<int> file;
        file.push_back(source);
        visite[source] = true;
        predecesseur[source] = -1;

        while (!file.empty())
        {
            int sommetCourant = file.front();
            file.pop_front();

            for (int i = 1; i < MAX; i++)
            {
              // Vérification des arcs non visités et ayant une capacité > 0
                if (!visite[i] && matriceCapacite[sommetCourant][i] > 0)
                {
                  // Si on atteint le sommet cible, on a trouvé un chemin augmentant
                    if (i == cible)
                    {
                        predecesseur[i] = sommetCourant;
                        return true;
                    }
                    file.push_back(i);
                    predecesseur[i] = sommetCourant;
                    visite[i] = true;
             }
            } }
        return false;
    }

    void fordFulkerson(int source, int cible)
    {
        int flotMax = 0;
        int capaciteMin;

        while (CheminAugmentant(source, cible))
        {
            capaciteMin = matriceCapacite[predecesseur[cible]][cible];

            for (int i = cible; i != source; i = predecesseur[i])
            {
              // Recherche de la capacité minimale sur le chemin augmentant
                if (capaciteMin > matriceCapacite[predecesseur[i]][i])
                    capaciteMin = matriceCapacite[predecesseur[i]][i];
            }

            for (int i = cible; i != source; i = predecesseur[i])
            {
              // Mise à jour des capacités résiduelles des arcs sur le chemin augmentant
                matriceCapacite[predecesseur[i]][i] -= capaciteMin;
                matriceCapacite[i][predecesseur[i]] += capaciteMin;
            }

            flotMax += capaciteMin;
        }

        cout << "Flot max = " << flotMax << endl;
    }
};

int main()
{
    Graphe graphe;
    int nbArc;

    cout << "Entrez le nombre d'arcs : ";
    cin >> nbArc;

    for (int i = 0; i < nbArc; i++)
    {
        cout << "Arc " << i+1 << " : " << endl;
        int source, destination, capacite;
        cout << "Sommet source : ";
        cin >> source;
        cout << "Sommet destination : ";
        cin >> destination;
        cout << "Capacité : ";
        cin>> capacite;

        graphe.ajouterArc(source, destination, capacite);
    }

    cout<<" *** *** *** *** ***"<<endl;

    int sommetDepart, sommetCible;
    cout << "Sommet source : ";
    cin >> sommetDepart;
    cout << "Sommet cible : ";
    cin >> sommetCible;

    graphe.fordFulkerson(sommetDepart, sommetCible);

    return 0;
}

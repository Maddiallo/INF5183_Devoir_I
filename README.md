Ce Devoir implémente les algorithmes de recherche suivants:

- **DFS** (Depth-First Search) – recherche en profondeur. 
- **BFS** (Breadth-First Search) – recherche en largeur 
- **A\*** avec **heuristique de Manhattan**
- Le labyrinthe est représenté par une grille 16×16 contenant :

- `#` : mur (obstacle infranchissable),
- `.` : case libre,
- `S` : point de départ,
- `G` : point d’arrivée.

L’agent se déplace uniquement dans les quatre directions (haut, bas, gauche, droite), avec un **coût uniforme de 1 par déplacement**.
L’objectif est de trouver un chemin de `S` à `G` et de comparer les performances des trois algorithmes.



##  Structure du devoir

Le devoir est structuré comme suit:

```text
Devoir_I/
├── maze.py       # Génération et gestion du labyrinthe
├── dfs.py        # Implémentation de DFS (pile LIFO)
├── bfs.py        # Implémentation de BFS (file FIFO)
├── astar.py      # Implémentation de A* (heuristique de Manhattan)
├── main.py       # Point d'entrée principal
└── README.md     # Explicqtion du devoir

Le programme s'execute dans Python 3.11 

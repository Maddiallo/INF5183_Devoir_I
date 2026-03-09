import time
from typing import Tuple, List, Set, Dict

Coord = Tuple[int, int]


def dfs(maze) -> Tuple[List[Coord], Set[Coord], int, float]:
    """
    Depth-First Search (Recherche en profondeur).
    Utilise une pile (LIFO).

    Retourne :
    - path      : liste des coordonnées du chemin S -> G (vide si pas de chemin)
    - visited   : ensemble des cases explorées
    - explored  : nombre de noeuds explorés
    - duration  : temps d'exécution en millisecondes
    """
    start: Coord = (1, 1)
    goal: Coord = (maze.size - 2, maze.size - 2)

    stack: List[Coord] = [start]
    visited: Set[Coord] = set()
    parent: Dict[Coord, Coord] = {}
    explored = 0

    start_time = time.perf_counter()

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        explored += 1

        if node == goal:
            break

        # Ajout des voisins dans l'ordre imposé
        for neighbor in maze.get_neighbors(*node):
            if neighbor not in visited and neighbor not in stack:
                stack.append(neighbor)
                # On ne met le parent qu'une seule fois
                if neighbor not in parent:
                    parent[neighbor] = node

    end_time = time.perf_counter()
    duration_ms = (end_time - start_time) * 1000.0

    path = _reconstruct_path(parent, start, goal)

    return path, visited, explored, duration_ms


def _reconstruct_path(parent: Dict[Coord, Coord], start: Coord, goal: Coord) -> List[Coord]:
    """
    Reconstruit le chemin à partir du dictionnaire parent.
    Retourne une liste vide si goal n'est pas atteignable.
    """
    if start == goal:
        return [start]

    if goal not in parent:
        return []

    path: List[Coord] = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

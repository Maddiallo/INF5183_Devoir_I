from collections import deque
import time
from typing import Tuple, List, Set, Dict

Coord = Tuple[int, int]


def bfs(maze) -> Tuple[List[Coord], Set[Coord], int, float]:
    """
    Breadth-First Search (recherche en largeur).
    Garantit le plus court chemin en nombre de pas.

    Retourne :
    - path      : liste des coordonnées du chemin S -> G (vide si pas de chemin)
    - visited   : ensemble des cases explorées
    - explored  : nombre de noeuds explorés
    - duration  : temps d'exécution en millisecondes
    """
    start: Coord = (1, 1)
    goal: Coord = (maze.size - 2, maze.size - 2)

    queue: deque[Coord] = deque([start])
    visited: Set[Coord] = {start}
    parent: Dict[Coord, Coord] = {}
    explored = 0

    start_time = time.perf_counter()

    while queue:
        node = queue.popleft()
        explored += 1

        if node == goal:
            break

        for neighbor in maze.get_neighbors(*node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
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

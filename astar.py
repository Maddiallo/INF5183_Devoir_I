import heapq
import time
from typing import Tuple, List, Set, Dict

Coord = Tuple[int, int]


def manhattan(a: Coord, b: Coord) -> int:
    """Distance de Manhattan (heuristique admissible)."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(maze) -> Tuple[List[Coord], Set[Coord], int, float]:
    """
    Algorithme A* (A-star).
    f(n) = g(n) + h(n) avec h = distance de Manhattan.

    Retourne :
    - path      : liste des coordonnées du chemin S -> G (vide si pas de chemin)
    - visited   : ensemble des cases explorées (noeuds fermés)
    - explored  : nombre de noeuds explorés
    - duration  : temps d'exécution en millisecondes
    """
    start: Coord = (1, 1)
    goal: Coord = (maze.size - 2, maze.size - 2)

    open_list: List[Tuple[int, Coord]] = []
    heapq.heappush(open_list, (0, start))

    g_cost: Dict[Coord, int] = {start: 0}
    parent: Dict[Coord, Coord] = {}
    visited: Set[Coord] = set()
    explored = 0

    start_time = time.perf_counter()

    while open_list:
        _, node = heapq.heappop(open_list)

        if node in visited:
            continue

        visited.add(node)
        explored += 1

        if node == goal:
            break

        for neighbor in maze.get_neighbors(*node):
            tentative_g = g_cost[node] + 1  # coût uniforme par mouvement

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f = tentative_g + manhattan(neighbor, goal)
                heapq.heappush(open_list, (f, neighbor))
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

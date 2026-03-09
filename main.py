from typing import List, Tuple, Set

from maze import Maze
from dfs import dfs
from bfs import bfs
from astar import astar

Coord = Tuple[int, int]


def print_solution(maze: Maze, path: List[Coord], visited: Set[Coord]) -> None:
    """
    Affiche une copie du labyrinthe avec :
    - 'p' pour les cases explorées
    - '*' pour le chemin solution
    """
    grid_copy = [row[:] for row in maze.grid]

    for x, y in visited:
        if grid_copy[x][y] == '.':
            grid_copy[x][y] = 'p'

    for x, y in path:
        if grid_copy[x][y] not in ('S', 'G'):
            grid_copy[x][y] = '*'

    for row in grid_copy:
        print(" ".join(row))
    print()


def main() -> None:
    maze = Maze(size=16, seed=42)

    print("LABYRINTHE INITIAL")
    maze.display()

    algorithms = [
        ("DFS", dfs),
        ("BFS", bfs),
        ("A* (manhattan)", astar),
    ]

    results: List[Tuple[str, int, int, float]] = []

    for name, algo in algorithms:
        print(f"===== {name} =====")
        path, visited, nodes, exec_time = algo(maze)

        # Affichage exploration + solution
        print_solution(maze, path, visited)

        path_length = len(path) if path else 0

        # === Affichage du chemin conforme au PDF ===
        if path:
            formatted_path = []

            for i, coord in enumerate(path):
                if i == 0:
                    formatted_path.append(f"S{coord}")
                elif i == len(path) - 1:
                    formatted_path.append(f"G{coord}")
                else:
                    formatted_path.append(str(coord))

            print("Chemin :", " -> ".join(formatted_path))
        else:
            print("Chemin : Aucun chemin trouvé")

        print("Noeuds explorés :", nodes)
        print("Longueur :", path_length)
        print("Temps (ms) :", round(exec_time, 3))
        print()

        results.append((name, nodes, path_length, round(exec_time, 3)))

    # === Tableau comparatif ===
    print("TABLEAU COMPARATIF")
    print("Algorithme       Noeuds   Longueur   Temps (ms)")
    print("------------------------------------------------")

    for name, nodes, length, t in results:
        print(f"{name:<15} {nodes:<7} {length:<9} {t}")


if __name__ == "__main__":
    main()
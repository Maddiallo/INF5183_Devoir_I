import random
from typing import List, Tuple, Optional

WALL = '#'
FREE = '.'
START = 'S'
GOAL = 'G'

Coord = Tuple[int, int]


class Maze:
    """
    Classe représentant un labyrinthe 2D.
    - '#' : mur
    - '.' : case libre
    - 'S' : départ
    - 'G' : objectif
    """

    def __init__(self, size: int = 16, seed: Optional[int] = None, wall_prob: float = 0.3):
        if size < 5:
            raise ValueError("La taille du labyrinthe doit être au moins 5.")
        self.size = size
        self.wall_prob = wall_prob

        if seed is not None:
            random.seed(seed)

        self.start: Coord = (1, 1)
        self.goal: Coord = (size - 2, size - 2)
        self.grid: List[List[str]] = self._generate_maze()

    def _generate_maze(self) -> List[List[str]]:
        """
        Génère un labyrinthe avec :
        - Bordures fermées
        - Murs aléatoires internes
        - Chemin garanti entre S et G
        """
        size = self.size

        # 1. Initialisation avec murs
        grid = [[WALL for _ in range(size)] for _ in range(size)]

        # 2. Création des cellules internes aléatoires
        for i in range(1, size - 1):
            for j in range(1, size - 1):
                grid[i][j] = FREE if random.random() > self.wall_prob else WALL

        # 3. Placement Start et Goal
        sx, sy = self.start
        gx, gy = self.goal
        grid[sx][sy] = FREE   # on les met libres d'abord
        grid[gx][gy] = FREE

        # 4. Garantie d'un chemin simple (carving direct)
        x, y = sx, sy
        while x < gx:
            x += 1
            grid[x][y] = FREE
        while y < gy:
            y += 1
            grid[x][y] = FREE

        # 5. Marquage final de S et G
        grid[sx][sy] = START
        grid[gx][gy] = GOAL

        return grid

    def display(self) -> None:
        """Affiche le labyrinthe."""
        for row in self.grid:
            print(" ".join(row))
        print()

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.size and 0 <= y < self.size

    def get_neighbors(self, x: int, y: int) -> List[Coord]:
        """
        Retourne les voisins accessibles
        Ordre imposé : droite, bas, gauche, haut
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors: List[Coord] = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.in_bounds(nx, ny) and self.grid[nx][ny] != WALL:
                neighbors.append((nx, ny))

        return neighbors

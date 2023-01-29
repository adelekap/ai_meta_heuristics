from typing import Set, Tuple, List

from dfs.maze_solver.generate_maze import MazeGenerator
from dfs.maze_solver.maze_location import MazeLocation
from dfs.maze_solver.maze_solver import MazeSolver


def solve_maze(size: int, walls: Set[Tuple[int, int]]) -> List[MazeLocation]:
    generator = MazeGenerator(size, walls)
    generator.generate()

    solver = MazeSolver(generator.start, generator.end)
    return solver.solve()


if __name__ == '__main__':
    SIZE = 5
    WALLS = {(0, 2), (1, 0), (2, 2), (2, 3), (2, 4), (3, 1), (3, 4)}

    print(solve_maze(SIZE, WALLS))

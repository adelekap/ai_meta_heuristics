from dfs.maze_solver.generate_maze import MazeGenerator
from dfs.maze_solver.maze_solver import MazeSolver

size = 5
walls = {(0, 2), (1, 0), (2, 2), (2, 3), (2, 4), (3, 1), (3, 4)}
generator = MazeGenerator(size, walls)
generator.generate()

solver = MazeSolver(generator.start, generator.end)
print(solver.solve())

from typing import List

from dfs.maze_solver.maze_exception import UnsolvableMazeException
from dfs.maze_solver.maze_location import MazeLocation


class MazeSolver:
    def __init__(self, starting_location: MazeLocation, goal: MazeLocation):
        self.starting_location = starting_location
        self.goal = goal

    def _search(self, path: List[MazeLocation]) -> List[MazeLocation]:
        visiting_location = path[-1]

        if visiting_location == self.goal:
            return path

        visiting_location.visited = True
        print(f'searched {visiting_location}')

        for adjacent_loc in visiting_location.adjacent_locations:
            if not adjacent_loc.visited and adjacent_loc.open:
                path = self._search(path + [adjacent_loc])
                return path

    def solve(self):
        path = self._search([self.starting_location])

        if path[-1] != self.goal:
            raise UnsolvableMazeException()

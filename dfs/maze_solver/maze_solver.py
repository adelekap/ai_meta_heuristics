from typing import List

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
        return self._search([self.starting_location])


if __name__ == '__main__':
    l_0_0 = MazeLocation(0, 0, True)
    l_0_1 = MazeLocation(0, 1, True)
    l_0_2 = MazeLocation(0, 2, True)
    l_1_0 = MazeLocation(1, 0, True)
    l_1_1 = MazeLocation(1, 1, False)
    l_1_2 = MazeLocation(1, 2, False)
    l_2_0 = MazeLocation(2, 0, True)
    l_2_1 = MazeLocation(2, 1, True)
    l_2_2 = MazeLocation(2, 2, True)

    l_0_0.adjacent_locations = [l_1_0, l_0_1]
    l_0_1.adjacent_locations = [l_0_0, l_0_2, l_1_1]
    l_0_2.adjacent_locations = [l_0_1, l_1_2]
    l_1_0.adjacent_locations = [l_0_0, l_1_1, l_2_0]
    l_1_1.adjacent_locations = [l_0_1, l_1_0, l_1_2, l_2_1]
    l_1_2.adjacent_locations = [l_0_2, l_1_1, l_2_2]
    l_2_0.adjacent_locations = [l_1_0, l_2_1]
    l_2_1.adjacent_locations = [l_2_0, l_1_1, l_2_2]
    l_2_2.adjacent_locations = [l_2_1, l_1_2]

    solver = MazeSolver(l_0_0, l_2_2)

    print(f'solution: {solver.solve()}')

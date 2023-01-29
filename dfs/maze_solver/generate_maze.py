from typing import Set, Tuple, List

from dfs.maze_solver.maze_location import MazeLocation


class MazeGenerator:
    def __init__(self, size: int, walls: Set[Tuple[int, int]]):
        self.size: int = size
        self.walls: Set[Tuple[int, int]] = walls

        self.locations = [[MazeLocation(x, y, (x, y) not in walls) for y in range(size)] for x in range(size)]

    @property
    def start(self) -> MazeLocation:
        return self.locations[0][0]

    @property
    def end(self) -> MazeLocation:
        return self.locations[-1][-1]

    def _neighbors(self, location: MazeLocation) -> List[MazeLocation]:
        up = (location.x - 1, location.y) if location.x > 0 else None
        down = (location.x + 1, location.y) if location.x < self.size - 1 else None
        left = (location.x, location.y - 1) if location.y > 0 else None
        right = (location.x, location.y + 1) if location.y < self.size - 1 else None

        return [self.locations[l[0]][l[1]] for l in [up, down, left, right] if l]

    def generate(self):
        for row in self.locations:
            for loc in row:
                loc.adjacent_locations = self._neighbors(loc)

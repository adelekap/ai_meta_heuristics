from typing import List


class MazeLocation:
    def __init__(self, x: int, y: int, open: bool):
        self.x: int = x
        self.y: int = y
        self.open: bool = open
        self.visited: bool = False

        self.adjacent_locations: List['MazeLocation'] = []

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return str(self)
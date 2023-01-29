from typing import List


class Node:
    def __init__(self, name: str):
        self.name: str = name
        self.adjacent_nodes: List['Node'] = []
        self.visited = False

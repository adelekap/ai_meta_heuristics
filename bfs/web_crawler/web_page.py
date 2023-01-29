from bfs.node import Node


class WebPage(Node):
    def __init__(self, url: str):
        super().__init__(url)

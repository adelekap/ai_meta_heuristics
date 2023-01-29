class UnsolvableMazeException(Exception):
    def __str__(self) -> str:
        return "Maze cannot be solved"

from bfs.node import Node


def breadth_first_search(starting_node: Node):
    queue = [starting_node]

    while queue:
        visiting_node = queue.pop(0)
        visiting_node.visited = True
        print(visiting_node.name)

        for neighbor in visiting_node.adjacent_nodes:
            if not neighbor.visited:
                queue.append(neighbor)


if __name__ == '__main__':
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')

    a.adjacent_nodes = [b, c]
    b.adjacent_nodes = [e, d]
    e.adjacent_nodes = [f]

    breadth_first_search(a)
from bfs.node import Node


def depth_first_search_iterative(starting_node: Node):
    stack = [starting_node]

    while stack:
        visiting_node = stack.pop(-1)
        visiting_node.visited = True
        print(f'searched {visiting_node.name}')

        for neighbor in visiting_node.adjacent_nodes:
            if not neighbor.visited:
                stack.append(neighbor)


def depth_first_search_recursive(node: Node):
    node.visited = True
    print(node.name)

    for adjacent_node in node.adjacent_nodes:
        if not adjacent_node.visited:
            depth_first_search_recursive(adjacent_node)


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

    depth_first_search_iterative(a)

    depth_first_search_recursive(a)

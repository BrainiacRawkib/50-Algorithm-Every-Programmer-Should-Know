"""
Breadth First Search Algorithm
"""

def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            neighbors = graph[node]

            # Only add neighbors to the queue that have not been visited yet
            unvisited_neighbors = [neighbor for neighbor in neighbors if neighbor not in visited]
            queue.extend(unvisited_neighbors)
    return visited


if __name__ == '__main__':
    graph: dict = {
        'Amin': {'Wasim', 'Nick', 'Mike'},
        'Wasim': {'Imran', 'Amin'},
        'Imran': {'Wasim', 'Faras'},
        'Faras': {'Imran'},
        'Mike': {'Amin'},
        'Nick': {'Amin'}
    }

    print(bfs(graph, 'Amin'))

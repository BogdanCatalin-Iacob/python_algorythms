'''
Breadth First Search and 
BFS shortest path implementation
'''

def bfs(graph, start_node):
    '''
    graph search algorithm
    returns a list of all the nodes in a graph
    '''

    visited_nodes = []
    # initialize nodes queue with search starting node
    queue = [start_node]

    while queue:
        current_node = queue.pop(0)
        visited_nodes.append(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited_nodes:
                queue.append(neighbor)
    
    return visited_nodes


def bfs_shortest_path(graph, start_node, end_note):
    '''
    bfs shortest path implementation,
    takes a graph a starting point and an end point
    to find the shortest path between them
    '''

    visited_nodes = []
    queue = [start_node]
    predecessor_nodes = {}

    while queue:
        current_node = queue.pop(0)
        visited_nodes.append(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited_nodes:
                queue.append(neighbor)
                predecessor_nodes[neighbor] = current_node
    
    print(shortest_path(predecessor_nodes, start_node, end_note))


def shortest_path(predecessor_node, start_node, end_note):
    '''
    create a path from predecessor nodes
    '''

    # start from end point (destination)
    path = [end_note]
    current_node = end_note

    while current_node != start_node:
        current_node = predecessor_node[current_node]
        path.append(current_node)
    
    # the path is in reverse order so it needs to be reversed
    path.reverse()
    return path

# test graph
the_graph = {
    '0': ['3', '5', '9'],
    '1': ['6', '7', '4'],
    '2': ['10', '5'],
    '3': ['0'],
    '4': ['1', '5', '8'],
    '5': ['2', '0', '4'],
    '6': ['1'],
    '7': ['1'],
    '8': ['4'],
    '9': ['0'],
    '10': ['2']
}


# print(bfs(the_graph, '0'))
bfs_shortest_path(the_graph, '10', '1')




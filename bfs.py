'''
Breadth First Search
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

print(bfs(the_graph, '0'))





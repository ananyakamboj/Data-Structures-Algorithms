from collections import defaultdict

edges = [
    ('A', 'B'),
    ('C', 'D'),
    ('E', 'F')
]

def createAdjacencyList(edges, direction = False):
    adjacency_list = defaultdict(list)
    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]
        adjacency_list[node1].append(node2)
        if not direction:
            adjacency_list[node2].append(node1)
        
    return adjacency_list

def bfs_Disconnected(adjacency_list, start):
    all_traversal = []
    visited = set()
    
    for node in adjacency_list.keys():
        if node not in visited:
            #perform bfs
            traversal = []
            queue = [node]
            
            while queue:
                front_node = queue.pop(0)
                if front_node not in visited:
                    visited.add(front_node)
                    traversal.append(front_node)
                    
                    #add neighbors
                    for neighbor in adjacency_list[front_node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
            all_traversal.extend(traversal)
    return all_traversal

adjacency_list = createAdjacencyList(edges, False)
bfs_traversal = bfs_Disconnected(adjacency_list,'A')
print('bfs_traversal', bfs_traversal)


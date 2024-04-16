import collections

edges = [(0,2),(2,1),(2,4),(4,3),(3,1)]

def createAdjacencyList(edges):
    adjacency_list = collections.defaultdict(list)
    for edge in edges:
        node1, node2 = edge
        adjacency_list[node1].append(node2)
        adjacency_list[node2].append(node1)
    return adjacency_list

def dfs(node, visited, adjacency_list, traversal):
    if node not in visited:
        traversal.append(node)
        visited.add(node)
        for neighbor in adjacency_list[node]:
            if neighbor not in visited:
                dfs(neighbor, visited, adjacency_list, traversal)
        
def dfsTraversal(adjacency_list):
    visited = set()
    traversal = []
    for vertex in adjacency_list.keys():
        if vertex not in visited:
            dfs(vertex, visited, adjacency_list, traversal)
    return traversal

adjacency_list = createAdjacencyList(edges)
dfs_traversal = dfsTraversal(adjacency_list)
print(dfs_traversal)

edges = []
adjacency_list = createAdjacencyList(edges)
dfs_traversal = dfsTraversal(adjacency_list)
print(dfs_traversal)

edges = [(1, 2), (2, 3)]
adjacency_list = createAdjacencyList(edges)
dfs_traversal = dfsTraversal(adjacency_list)
print(dfs_traversal)

# DISCONNECTED GRAPH
edges = [(1, 2), (3, 4), (5, 6)]
adjacency_list = createAdjacencyList(edges)
dfs_traversal = dfsTraversal(adjacency_list)
print(dfs_traversal)

# TREE GRAPH
edges = [(1, 2), (1, 3), (2, 4), (2, 5)]
adjacency_list = createAdjacencyList(edges)
dfs_traversal = dfsTraversal(adjacency_list)
print(dfs_traversal)

# With self loops
edges = [(1, 2), (2, 3), (3, 3), (1, 1)]
adjacency_list = createAdjacencyList(edges)
dfs_traversal = dfsTraversal(adjacency_list)
print(dfs_traversal)
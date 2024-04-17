# Cycle detection using DFS
import collections

# Step 1: Create an adjacency list
def createAdjacencyList(edges, direction = False):
    adjacency_list = collections.defaultdict(list)
    for edge in edges:
        node1, node2 = edge
        adjacency_list[node1].append(node2)
        if not direction:
            adjacency_list[node2].append(node1)
    return adjacency_list

#STEP 2: Create isCycle function
def isCycle(adjacency_list):
    visited = set()
    parent = collections.defaultdict(lambda: None)
    answer = False
    for vertex in adjacency_list:
        if vertex not in visited:
            answer |= dfs(vertex, adjacency_list, parent, visited)
            if answer == True:
                return True
    return False

# STEP 3: Create DFS function
def dfs(node, adjacency_list, parent, visited):
    visited.add(node)          
    for neighbor in adjacency_list[node]:
        if neighbor not in visited:
            parent[neighbor] = node
            if dfs(neighbor, adjacency_list, parent, visited):
                return True
        elif neighbor != parent[node]:
            return True
    return False

edges = []
adj_list = createAdjacencyList(edges)
answer = isCycle(adj_list)           
print(answer)

edges = [(1, 2), (2, 3)]
adj_list = createAdjacencyList(edges)
answer = isCycle(adj_list)           
print(answer)

edges = [(1, 2), (2, 3),(3,1)]
adj_list = createAdjacencyList(edges)
answer = isCycle(adj_list)           
print(answer)

edges = [(1, 2), (3, 4), (5, 6),(6,7),(7,5)]
adj_list = createAdjacencyList(edges)
answer = isCycle(adj_list)           
print(answer)
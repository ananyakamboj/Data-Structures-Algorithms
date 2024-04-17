# step 1: create adjacency list
import collections

def createAdjacencyList(edges, direction = True):
    adjacency_list = collections.defaultdict(list)
    for edge in edges:
        node1, node2 = edge
        adjacency_list[node1].append(node2)
        if not direction:
            adjacency_list[node2].append(node1)
    return adjacency_list

# step 2: Create visited set, dfs_traversal algorithm, dfs_call hashmap

def dfs_traversal(node, adjacency_list, visited, dfs_call):
    visited.add(node)
    dfs_call[node] = True  
    for neighbor in adjacency_list[node]:
        if neighbor not in visited:
            ans = dfs_traversal(neighbor, adjacency_list, visited, dfs_call)
            if ans == True:
                return True
        elif dfs_call[node] == True:
            return True
        
    dfs_call[node] = False
    return False

# step 3: Loop through all the vertices of graph which are not visited.

def directedGraphDFS(adjacency_list):
    visited = set()
    dfs_call = collections.defaultdict(bool)
    
    for vertex in list(adjacency_list.keys()):
        if vertex not in visited:
            if dfs_traversal(vertex,adjacency_list, visited, dfs_call):
                return True
    return False            

edges = [(1, 2), (2, 3), (3, 4)]
adj_list = createAdjacencyList(edges)
answer = directedGraphDFS(adj_list)
print(answer)
# cycle detection in a graph
import collections

# Step 1: Create adjacency list
def createAdjacencyList(edges, direction = False):
    adjacency_list = collections.defaultdict(list)
    for edge in edges:
        node1, node2 = edge
        adjacency_list[node1].append(node2)
        if not direction:
            adjacency_list[node2].append(node1)
    return adjacency_list

# Step 2: Create a function to check isCycle
def isCycle(adjacency_list):
    visited = set()
    parent = collections.defaultdict(lambda: None)
    answer = False
    for vertex in adjacency_list.keys():
        if vertex not in visited:
            answer |= bfs(vertex, adjacency_list, visited, parent)
            if answer == True:
                return True
    return False

# Step 3: Add the BFS function
def bfs(node, adjacency_list, visited, parent):
    queue = [node]
    while queue:
        node = queue.pop(0)
        visited.add(node)
        for neighbor in adjacency_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = node
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


edges = [(1, 2), (2, 3), (3, 4)]
adj_list = createAdjacencyList(edges, False)
answer = isCycle(adj_list)           
print(answer)


from collections import defaultdict

# List of edges provided as a question
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E'),
    ('C', 'F'),
    ('E', 'F')
]

# STEP 1: CREATE AN ADJACENCY LIST

def createAdjacencyList(edges, direction = False):
    adjacency_list = defaultdict(list)
    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]
        adjacency_list[node1].append(node2)
        if not direction:
            adjacency_list[node2].append(node1)
    return adjacency_list

def displayAdjacencyList(adjacency_list):
    for k, v in adjacency_list.items():
        print(k, ":", v)
adjacency_list = createAdjacencyList(edges, False)
vertices = len(adjacency_list.keys())
number_of_edges = len(edges)

# Step 1: Create an adjacency list.
# Step 2: Create a set for visited, queue for node traversal and a list to give as output.
# Step 3: Initialize the queue with the first element of the adjacency list.
# Step 4: Pop the first element of the queue.
#       i. Mark the node as visited.
#       ii. Add it to the traversal list.
# Step 5: Loop through the neighbors. If the neighbor is not visited, then add it to the queue.

def bfs(adjacency_list, start_node):
    traversal = []
    visited = set()
    queue = [start_node]
    
    while queue:
        print("queue", queue)
        front_node = queue.pop(0)
        visited.add(front_node)
        traversal.append(front_node)
        
        # print("visited", visited)
        # print("traversal", traversal, "\n")
        for neighbor in adjacency_list[front_node]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
    
    return traversal

bfs_traversal = bfs(adjacency_list, 'A')
print("bfs_traversal", bfs_traversal)

# EXAMPLE 2: CYCLIC GRAPH
edges2 = [
    ('1', '2'),
    ('1', '3'),
    ('2', '4'),
    ('2', '5'),
    ('3', '6'),
    ('4', '7'),
    ('4', '8'),
    ('5', '9'),
    ('5', '10'),
    ('6', '1'),  # This creates a cycle in the graph
    ('7', '8')   # This creates a cycle in the graph
]
adjacency_list = createAdjacencyList(edges2, False)
print(adjacency_list)
bfs_traversal = bfs(adjacency_list, '1')
print("bfs_traversal", bfs_traversal)

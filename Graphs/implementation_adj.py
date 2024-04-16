# GRAPH IMPLEMENTATION USING ADJACENCY LIST
class Graph:
    # initializing the graph with adjacency list
    def __init__(self) -> None:
        self.adjacency_list = {}
    
    # adding a node to the graph
    def addNode(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
        
    # adding edges to the graph
    def addEdge(self, node1, node2, direction = False):
        self.adjacency_list[node1].append(node2)
        if not direction:
            self.adjacency_list[node2].append(node1)
    
    def displayAdjacencyList(self):
        for k,v in self.adjacency_list.items():
            print(k, ":", v)

        

graph = Graph()
for i in range(5):
    graph.addNode(i)
graph.addEdge(0,1)
graph.addEdge(0,4)
graph.addEdge(1,2)
graph.addEdge(1,3)
graph.addEdge(2,3)
graph.addEdge(3,4)
graph.displayAdjacencyList()
    
    
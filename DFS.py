# Depth First Search Algorithm

def dfs(graph, starting_node, visited=None):
    if visited is None:
        visited = set()
    visited.add(starting_node)
    
    for next_node in graph[starting_node] - visited:
        dfs(graph, next_node, visited)
    
    return visited
    
    
num_of_nodes = int(input("Enter number of nodes : "))

graph = [[] for _ in range(num_of_nodes)]  # Initialize empty graph

while True :
    edge = input()
    
    if edge == "done" or edge =="Done":
        break
    
    node1, node2 = map(int, edge.split())
    graph[node1].append(node2)
    graph[node2].append(node1)

print("The entered graph : ")
for node, edges in enumerate(graph):
    print(f"Node {node}: {edges}")
    
starting_node = int(input("Enter starting node : "))
    
dfs(graph, starting_node)
#print("Visited Nodes : ",result)
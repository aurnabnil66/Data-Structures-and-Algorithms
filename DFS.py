# Depth First Search Algorithm

visited = set()   # setting visited set as global
def dfs(graph, starting_node, visited):
    if starting_node not in visited:
        print(starting_node)
        visited.add(starting_node)
        for edge_node in graph[starting_node]:
            dfs(graph, edge_node, visited)
        
    
num_of_nodes = int(input("Enter number of nodes : "))
print("Enter nodes and edges like (node edge) : ")

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
    
dfs(graph, starting_node, visited)

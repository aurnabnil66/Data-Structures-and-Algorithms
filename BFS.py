# Breadth First Search Algorithm

visited = []   # setting visited set as global
queue = []

def bfs(graph, starting_node, visited):
    visited.append(starting_node)
    queue.append(starting_node)

    while queue:
        x = queue.pop(0)
        print(x, end=" ")
        for edge_node in graph[x]:
            if edge_node not in visited:
                visited.append(edge_node)
                queue.append(edge_node)
        

num_of_nodes = int(input("Enter number of nodes : "))
print("Enter nodes and edges like (node edge) : ")

graph = [[] for _ in range(num_of_nodes)]  # Initialize empty graph

while True:
    edge = input()

    if edge == "done" or edge == "Done":
        break

    node1, node2 = map(int, edge.split())
    graph[node1].append(node2)
    graph[node2].append(node1)

print("The entered graph : ")
for node, edges in enumerate(graph):
    print(f"Node {node}: {edges}")

starting_node = int(input("Enter starting node : "))

bfs(graph, starting_node, visited)

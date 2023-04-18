# Graph data structure implementation using Adjacency Matrix

vertices = []
num_of_vertices = 0
graph = []

# Adding a vertex to the vertices list
def add_vertex(v):
    global vertices
    global num_of_vertices
    global graph
    
    if v in vertices:
        print("Vertex ",v, " already exists")
    else:
        num_of_vertices += 1
        vertices.append(v)
        if num_of_vertices > 1:
            for vertex in graph:
                vertex.append(0)
        
        temp = []
        for x in range(num_of_vertices):
            temp.append(0)
        
        graph.append(temp)
    
# Adding an edge between two vertices
def add_edge(v1, v2, e):
    global vertices
    global num_of_vertices
    global graph
    
    if v1 not in vertices:
        print("Vertex ",v1, " does not exist")
    
    elif v2 not in vertices:
        print("Vertex ",v2, " does not exist")
        
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e
        
# Printing the graph
def print_graph():
    global vertices
    global num_of_vertices
    global graph
    
    for i in range(num_of_vertices):
        for j in range(num_of_vertices):
            if graph[i][j] != 0:
                print(vertices[i], " -> ", vertices[j], " edge weight : ", graph[i][j]) 


# Adding vertices
add_vertex("A")
add_vertex("B")
add_vertex("C")
add_vertex("D")
add_vertex("E")
add_vertex("F")

# Adding edges between specified vertices (node1, node2, edge value)
add_edge("A", "B", 2)
add_edge("B", "C", 3)
add_edge("C", "D", 1)
add_edge("A", "E", 6)
add_edge("E", "F", 4)
add_edge("F", "D", 5)

print_graph()
print("List representation Adjacency Matrix : ")
print(graph)
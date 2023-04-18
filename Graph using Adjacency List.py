# Graph data structure implementation using Adjacency Matrix

num_of_vertices = 0
graph = {}

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
print("Adjacency List : ")
print(graph)
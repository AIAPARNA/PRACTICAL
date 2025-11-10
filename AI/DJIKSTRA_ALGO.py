import heapq  # This is Python's priority queue module
import sys

# --- THIS IS THE CLASS YOU PROVIDED ---
class Graph:
    def __init__(self, vertices):
        """
        Initialize the graph with a given number of vertices.
        Vertices are assumed to be numbered 0 to vertices-1.
        """
        self.V = vertices
        # We use a dictionary to represent the adjacency list
        # self.adj[u] = {v: weight, w: weight, ...}
        self.adj = {i: {} for i in range(self.V)}

    def add_edge(self, u, v, weight):
        """
        Add a weighted, directed edge from vertex u to vertex v.
        For an undirected graph, add the edge in both directions.
        """
        # Add the edge
        self.adj[u][v] = weight
        
        # If the graph is undirected, uncomment the line below
        # self.adj[v][u] = weight

    def dijkstra(self, start_vertex):
        """
        Performs Dijkstra's single-source shortest path algorithm.
        :param start_vertex: The vertex to start from.
        :return: A dictionary of shortest distances from the start_vertex to all others.
        """
        
        # 1. Initialize distances
        distances = {vertex: float('inf') for vertex in range(self.V)}
        distances[start_vertex] = 0

        # 2. Initialize the priority queue
        priority_queue = [(0, start_vertex)] # (distance, vertex)

        while priority_queue:
            # 3. Pop the vertex with the smallest distance
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # 4. Check for outdated entries
            if current_distance > distances[current_vertex]:
                continue

            # 5. "Relax" all neighbors
            for neighbor, weight in self.adj[current_vertex].items():
                
                distance = current_distance + weight

                # 6. If we found a shorter path, update it
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        # 7. Return the final distances
        return distances

# --- BASIC MENU-DRIVEN PART ---

g = None  # Placeholder for our graph object

while True:
    print("\nDijkstra's Algorithm Menu")
    print("1. Create a new Graph")
    print("2. Add an Edge (directed)")
    print("3. Run Dijkstra's Algorithm")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        try:
            num_vertices = int(input("Enter the total number of vertices: "))
            if num_vertices <= 0:
                print("Error: Number of vertices must be positive.")
            else:
                g = Graph(num_vertices)
                print(f"Graph with {num_vertices} vertices (0 to {num_vertices-1}) created.")
        except ValueError:
            print("Error: Please enter a valid number.")

    elif choice == '2':
        if g is None:
            print("Error: Please create a graph first (Option 1).")
        else:
            try:
                u = int(input(f"  Enter source vertex (0 to {g.V - 1}): "))
                v = int(input(f"  Enter destination vertex (0 to {g.V - 1}): "))
                w = int(input("  Enter edge weight: "))
                
                if 0 <= u < g.V and 0 <= v < g.V:
                    g.add_edge(u, v, w)
                    print(f"Edge ({u} -> {v}) with weight {w} added.")
                else:
                    print(f"Error: Vertices must be between 0 and {g.V - 1}.")
            except ValueError:
                print("Error: Please enter valid numbers for vertices and weight.")

    elif choice == '3':
        if g is None:
            print("Error: Please create a graph first (Option 1).")
        else:
            try:
                start_v = int(input(f"Enter the source vertex to start from (0 to {g.V - 1}): "))
                
                if 0 <= start_v < g.V:
                    # Run the algorithm
                    shortest_paths = g.dijkstra(start_v)
                    
                    # Print the results
                    print(f"\n--- Shortest Paths from source vertex {start_v} ---")
                    for vertex, distance in shortest_paths.items():
                        if distance == float('inf'):
                            print(f"  Vertex {vertex}: No path exists")
                        else:
                            print(f"  Vertex {vertex}: Shortest distance is {distance}")
                    print("---------------------------------")
                else:
                    print(f"Error: Invalid source vertex. Must be 0 to {g.V - 1}.")
            except ValueError:
                print("Error: Please enter a valid number.")

    elif choice == '4':
        print("Exiting...")
        break  # Exit the while loop

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
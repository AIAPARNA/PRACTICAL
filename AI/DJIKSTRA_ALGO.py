import heapq

# --- GRAPH CLASS (UNCHANGED) ---
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: {} for i in range(self.V)}

    def add_edge(self, u, v, weight):
        self.adj[u][v] = weight
        # For undirected, add: self.adj[v][u] = weight

    def dijkstra(self, start_vertex):
        distances = {vertex: float('inf') for vertex in range(self.V)}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)] # (distance, vertex)

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.adj[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances

# --- MENU (EASIER TO UNDERSTAND) ---

g = None  # Graph object placeholder

while True:
    # A clear, multi-line menu
    print("\n--- Dijkstra's Algorithm Menu ---")
    print("  1. Create a New Graph")
    print("  2. Add an Edge")
    print("  3. Find Shortest Paths")
    print("  4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        try:
            num_vertices = int(input("How many vertices in your graph? "))
            if num_vertices > 0:
                g = Graph(num_vertices)
                # Clear confirmation message
                print(f"==> Graph with {num_vertices} vertices (0 to {num_vertices - 1}) created.")
            else:
                print("Error: Number of vertices must be positive.")
        except ValueError:
            print("Error: Please enter a valid number.")

    elif choice == '2':
        if g is None:
            print("Error: You must create a graph first (Option 1).")
        else:
            try:
                # Clearer prompts
                u = int(input(f"  Enter FROM vertex (0 to {g.V - 1}): "))
                v = int(input(f"  Enter TO vertex (0 to {g.V - 1}): "))
                w = int(input( "  Enter the WEIGHT of the edge: "))
                
                if 0 <= u < g.V and 0 <= v < g.V:
                    g.add_edge(u, v, w)
                    print(f"==> Edge added: {u} -> {v} (Weight: {w})")
                else:
                    # Clearer error
                    print(f"Error: Vertices must be between 0 and {g.V - 1}.")
            except ValueError:
                print("Error: Please enter valid numbers.")

    elif choice == '3':
        if g is None:
            print("Error: You must create a graph first (Option 1).")
        else:
            try:
                start_v = int(input(f"Enter the START vertex (0 to {g.V - 1}): "))
                
                if 0 <= start_v < g.V:
                    shortest_paths = g.dijkstra(start_v)
                    
                    # Clearer results formatting
                    print(f"\n--- Shortest Paths from Vertex {start_v} ---")
                    for vertex, distance in shortest_paths.items():
                        if distance == float('inf'):
                            print(f"  To Vertex {vertex}: No path found")
                        else:
                            print(f"  To Vertex {vertex}: Shortest distance is {distance}")
                    print("---------------------------------")
                else:
                    print(f"Error: Invalid start vertex. Must be 0 to {g.V - 1}.")
            except ValueError:
                print("Error: Please enter a valid number.")

    elif choice == '4':
        print("Goodbye!")
        break  # Exit the loop

    else:
        print("Error: Invalid choice. Please pick 1, 2, 3, or 4.")
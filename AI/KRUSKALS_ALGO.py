# --- Kruskal's Algorithm Class ---
# (This is the same core logic as before)
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.parent = []
        self.rank = []

    def add_edge(self, u, v, w):
        # Store as (weight, source, destination)
        self.graph.append([w, u, v])

    def _find(self, i):
        # Finds the root of i's set with path compression
        if self.parent[i] == i:
            return i
        self.parent[i] = self._find(self.parent[i])
        return self.parent[i]

    def _union(self, x_root, y_root):
        # Attaches the smaller rank tree to the higher rank tree
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

    def kruskal_mst(self):
        mst_result = []
        total_weight = 0
        
        # 1. Sort all edges by weight
        self.graph.sort()
        
        # 2. Initialize DSU
        self.parent = [i for i in range(self.V)]
        self.rank = [0] * self.V
        
        edge_count = 0
        edge_index = 0
        
        # 3. Loop until we have V-1 edges
        while edge_count < self.V - 1 and edge_index < len(self.graph):
            w, u, v = self.graph[edge_index]
            edge_index += 1
            
            root_u = self._find(u)
            root_v = self._find(v)
            
            # 4. Check for cycle
            if root_u != root_v:
                # No cycle, add edge to MST
                edge_count += 1
                mst_result.append((u, v, w))
                total_weight += w
                self._union(root_u, root_v)
        
        # 5. Print the result
        print("\n--- Minimum Spanning Tree (MST) ---")
        for u, v, weight in mst_result:
            print(f"  {u} -- {v} == {weight}")
        print(f"Total Minimum Weight: {total_weight}")
        print("-----------------------------------")
        
        # Check for connectivity
        if edge_count != self.V - 1:
            print("Note: The graph is not fully connected.")


# --- Basic Menu Driver ---

g = None  # We'll create the graph object later

while True:
    print("\n--- MENU ---")
    print("1. Create Graph")
    print("2. Add Edge")
    print("3. Find MST")
    print("4. Exit")
    
    # Assume user enters a valid number
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        num_vertices = int(input("Enter number of vertices: "))
        g = Graph(num_vertices)
        print(f"Graph with {num_vertices} vertices created.")

    elif choice == '2':
        if g is None:
            print("Please create a graph first (Option 1).")
        else:
            u = int(input("  Enter source vertex: "))
            v = int(input("  Enter destination vertex: "))
            w = int(input("  Enter edge weight: "))
            g.add_edge(u, v, w)
            print("Edge added successfully.")

    elif choice == '3':
        if g is None:
            print("Please create a graph first (Option 1).")
        elif not g.graph:
             print("Graph has no edges. Please add edges (Option 2).")
        else:
            g.kruskal_mst()

    elif choice == '4':
        print("Exiting...")
        break  # Exit the while loop

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
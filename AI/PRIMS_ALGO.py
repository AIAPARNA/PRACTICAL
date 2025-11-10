import heapq

def prims(graph, start):
    visited = set()
    parent = {v: None for v in graph}
    key = {v: float('inf') for v in graph}  # store min edge weight to each vertex
    key[start] = 0

    min_heap = [(0, start)]
    total_cost = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        # Skip if already visited
        if node in visited:
            continue

        visited.add(node)
        total_cost += weight

        for neighbor, w in graph[node]:
            if neighbor not in visited and w < key[neighbor]:
                key[neighbor] = w
                parent[neighbor] = node
                heapq.heappush(min_heap, (w, neighbor))

    print("\nEdges in Minimum Spanning Tree:")
    for node in parent:
        if parent[node] is not None:
            print(f"{parent[node]} - {node} (weight = {key[node]})")

    print(f"\nTotal Minimum Cost = {total_cost}")


def main():
    graph = {}

    while True:
        print("\n--- MENU ---")
        print("1. Add edge")
        print("2. Run Prim's Algorithm")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            u = input("Enter first vertex: ")
            v = input("Enter second vertex: ")
            w = int(input("Enter edge weight: "))

            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []

            graph[u].append((v, w))
            graph[v].append((u, w))
            print(f"Edge added: {u} --{w}--> {v}")

        elif choice == 2:
            if not graph:
                print("Graph is empty! Add edges first.")
                continue

            start = input("Enter starting vertex: ")
            if start not in graph:
                print("Invalid start vertex!")
                continue

            prims(graph, start)

        elif choice == 3:
            print("Exiting program.")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()

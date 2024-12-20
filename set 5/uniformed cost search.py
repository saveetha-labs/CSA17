import heapq

# Function to perform Uniform Cost Search (UCS)
def uniform_cost_search(graph, start, goal):
    # Priority queue to store (cost, node) pairs
    priority_queue = [(0, start)]
    # Dictionary to store the minimum cost to reach each node
    cost_so_far = {start: 0}
    # Dictionary to track the path
    parent = {start: None}

    while priority_queue:
        # Get the node with the lowest cost
        current_cost, current_node = heapq.heappop(priority_queue)

        # If the goal is reached, construct the path
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1], current_cost  # Return path and total cost

        # Explore neighbors of the current node
        for neighbor, edge_cost in graph[current_node]:
            new_cost = current_cost + edge_cost

            # If a cheaper path to neighbor is found, update the cost and queue
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                parent[neighbor] = current_node
                heapq.heappush(priority_queue, (new_cost, neighbor))

    return None, float('inf')  # Return None if goal is unreachable

# Example usage
if __name__ == "__main__":
    # Tree with weighted edges as an adjacency list
    graph = {
        'S': [('A', 1), ('B', 5)],
        'A': [('C', 3), ('D', 7)],
        'B': [('D', 2), ('G', 8)],
        'C': [('G', 4)],
        'D': [('G', 1)],
        'G': []
    }

    start_node = 'S'
    goal_node = 'G'

    # Perform UCS to find the path and cost from S to G
    path, total_cost = uniform_cost_search(graph, start_node, goal_node)

    # Output the results
    if path:
        print(f"Path: {' -> '.join(path)}")
        print(f"Total Cost: {total_cost}")
    else:
        print("Goal node not reachable from the start node.")

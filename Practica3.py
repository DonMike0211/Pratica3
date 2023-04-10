import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

# Ejemplo de uso
graph = {
    'A': {'B': 3, 'C': 4, 'D': 2},
    'B': {'E': 1},
    'C': {'F': 2},
    'D': {'G': 3},
    'E': {'H': 6},
    'F': {'H': 1},
    'G': {'H': 2},
    'H': {}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print(f"Distancias desde el nodo {start_node}: {distances}")


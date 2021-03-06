# Algoritmo Dijkstra(unvisited set, distances information, neighbours information, start vertex)
def dijsktra(unvisited: set, distances: dict, neighbours: dict, start: str):

    # Let distance of start vertex from start = 0. Let distance of all other vertices = infinity.
    known = { nodo: 0 if nodo == start else float('inf') for nodo in unvisited }
    # Let the previous node be unknown(none) for every vertex
    previous = { node: None for node in unvisited }

    # Repeat until there are no vertices left to visit:
    while len(unvisited)>0:
        # Visit the unvisited vertex with the smallest known distance from the start vertex
        distance, visit = min( [ (known[nodo], nodo) for nodo in unvisited ] )
        # For the current vertex, calculate the distance from the visited vertex to each of its neighbours
        calculated = { neighbour: distance + distances[visit, neighbour] for neighbour in neighbours[visit] if neighbour in unvisited }
        # Update previous and known distances if the calculated distance is less than the known distance
        known.update( { neighbour: calculated[neighbour] if calculated[neighbour] < known[neighbour] else known[neighbour] for neighbour in neighbours[visit] if neighbour in unvisited } )
        previous.update( { neighbour: visit if calculated[neighbour] < known[neighbour] else known[neighbour] for neighbour in neighbours[visit] if neighbour in unvisited } )
        # Remove the current vertex (visited) from the unvisited set.
        unvisited.remove(visit)
    # Return the best known distances and their corresponing previous nodes
    return known, previous


unvisited = {'A', 'B', 'C', 'D', 'E', 'C'}

distances = {('A', 'B'): 6, ('A', 'D'): 1, ('B', 'C'): 5, ('B', 'D'): 2, ('B', 'E'):2, ('D', 'E'): 1, ('E','C'): 5,
             ('B', 'A'): 6, ('D', 'A'): 1, ('C', 'B'): 5, ('D', 'B'): 2, ('E', 'B'):2, ('E', 'D'): 1, ('C','E'): 5}

neighbours = {
                'A': ['B', 'D'],
                'B': ['A', 'D', 'C'],
                'C': ['B', 'E'],
                'D': ['A', 'B', 'E'],
                'E': ['D', 'B', 'C']
              }

minima, predecesores = dijsktra(unvisited, distances, neighbours, 'A')
print(minima, predecesores)

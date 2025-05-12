#Поиск кратчайшего пути
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
            
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

import unittest

class TestDijkstra(unittest.TestCase):

    def test1(self):
        self.assertEqual(dijkstra({'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2}, 'C': {'A': 4, 'B': 2}}, 'A'), {'A': 0, 'B': 1, 'C': 3})

    def test2(self):
        self.assertEqual(dijkstra({'A': {'B': 1}, 'B': {'A': 1}, 'C': {'D': 1}, 'D': {'C': 1}}, 'A'), {'A': 0, 'B': 1, 'C': float('infinity'), 'D': float('infinity')})

    def test3(self):
        self.assertEqual(dijkstra({'A': {}}, 'A'), {'A': 0})

    def test4(self):
        self.assertEqual(dijkstra({'A': {'B': 5}, 'B': {'C': 3}, 'C': {'A': 1}}, 'A'), {'A': 0, 'B': 5, 'C': 8})
        
    def test5(self):
        self.assertEqual(dijkstra({'A': {'B': 2, 'C': 5}, 'B': {'A': 2, 'D': 3}, 'C': {'A': 5, 'D': 1}, 'D': {'B': 3, 'C': 1}}, 'A'), {'A': 0, 'B': 2, 'C': 5, 'D': 5})

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

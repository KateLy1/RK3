#Дан граф. Необходимо подсчитать
#количество компонент связности.
#Вариант 1
def dfs(graph, v, visited, component):
    visited[v] = True
    component.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, component)

def find_connected_components(graph):
    visited = {}
    for i in range(1, len(graph) + 1):
        visited[i] = False
    connected_components = []
    for node in graph:
        if not visited[node]:
            component = []
            dfs(graph, node, visited, component)
            connected_components.append(component)
    return connected_components

import unittest

class TestFind_connected_components(unittest.TestCase):

    def test1(self):
        self.assertEqual(find_connected_components({}), [])

    def test2(self):
        self.assertEqual(find_connected_components({1: []}), [[1]])

    def test3(self):
        self.assertEqual(find_connected_components({1: [], 2: []}), [[1], [2]])

    def test4(self):
        self.assertEqual(find_connected_components({1: [2, 3], 2: [1, 3], 3: [1, 2]}), [[1, 2, 3]])
        
    def test5(self):
        self.assertEqual(find_connected_components({1: [2], 2: [1], 3: [4], 4: [3], 5: []}), [[1, 2], [3, 4], [5]])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Вариант 2
def dfs(graph, v, visited, color):
    visited[v] = color
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited, color)

def find_connected_components2(graph):
    visited = {}
    for i in range(1, len(graph) + 1):
        visited[i] = 0
    color = 0
    for node in graph:
        if visited[node] == 0:
            color += 1
            dfs(graph, node, visited, color)
    return visited


import unittest

class TestFind_connected_components2(unittest.TestCase):

    def test1(self):
        self.assertEqual(find_connected_components2({}), {})

    def test2(self):
        self.assertEqual(find_connected_components2({1: []}), {1: 1})

    def test3(self):
        self.assertEqual(find_connected_components2({1: [], 2: []}), {1: 1, 2: 2})

    def test4(self):
        self.assertEqual(find_connected_components2({1: [2, 3], 2: [1, 3], 3: [1, 2]}), {1: 1, 2: 1, 3: 1})
        
    def test5(self):
        self.assertEqual(find_connected_components2({1: [2], 2: [1], 3: [4], 4: [3], 5: []}), {1: 1, 2: 1, 3: 2, 4: 2, 5: 3})

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

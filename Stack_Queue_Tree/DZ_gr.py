# Реализация графа с использованием списков смежности

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        """Добавляет вершину в граф"""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Добавляет ребро между двумя вершинами"""
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # Это нужно удалить для ориентированного графа

    def remove_edge(self, vertex1, vertex2):
        """Удаляет ребро между двумя вершинами"""
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        """Удаляет вершину и все связанные с ней ребра"""
        if vertex in self.graph:
            for adjacent in self.graph[vertex]:
                self.graph[adjacent].remove(vertex)
            del self.graph[vertex]

    def get_vertices(self):
        """Возвращает список всех вершин в графе"""
        return list(self.graph.keys())

    def get_edges(self):
        """Возвращает список всех рёбер в графе"""
        edges = []
        for vertex in self.graph:
            for adjacent in self.graph[vertex]:
                if {vertex, adjacent} not in edges:
                    edges.append({vertex, adjacent})
        return edges

    def __str__(self):
        """Возвращает строковое представление графа"""
        result = ""
        for vertex in self.graph:
            result += f"{vertex}: {', '.join(map(str, self.graph[vertex]))}\n"
        return result

# Пример использования
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")

print("Вершины графа:", g.get_vertices())
print("Рёбра графа:", g.get_edges())
print("Граф:\n", g)

g.remove_edge("A", "B")
print("После удаления ребра (A, B):\n", g)

g.remove_vertex("C")
print("После удаления вершины C:\n", g)
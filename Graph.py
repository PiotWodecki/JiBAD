class Graph:

    def __init__(self, start_graph = None):
        if start_graph != None:
            self.graph = start_graph
        else:
            self.graph = dict()

    @staticmethod
    def add_vertex(self, node): # to nie może być metoda statyczna
        if node not in self.graph.keys():   # równoważne node not in self.graph - używać wg. uznania
            self.graph[node] = []

    def delete_vertex(self, node):
        if node in self.graph.keys():
            self.graph.pop(node, None)

    def add_connection(self, node_from, node_to):
        if node_from in self.graph.keys() and node_to in self.graph.keys() and node_from != node_to:
            if node_to not in self.graph[node_from]:
                self.graph[node_from].append(node_to)
            if node_from not in self.graph[node_to]:
                self.graph[node_to].append(node_from)
            #self.graph.update(dict(node_from)=)

    def remove_connection(self, node_from, node_to):
        if node_from in self.graph.keys() and node_to in self.graph.keys() and node_from != node_to:
            self.graph[node_from].remove(node_to)
            self.graph[node_to].remove(node_from)

    def get_all_neighbours_of_node(self, node):
        try:
            if node in self.graph.keys():
                return self.graph[node]

        except:
            "error" # ucisza Pan wszystkie wyjątki; nie wolno robić czegoś takiego bez b. dobrego powodu (a b. dobry powód wymaga komentarza)
# brak DFS i BFS

graph = Graph()
graph.add_vertex(graph, 'A')
graph.add_vertex(graph,'B')
graph.add_vertex(graph, 'C')
graph.add_vertex(graph, 'D')
graph.add_vertex(graph, 'E')

graph.add_connection('B', 'C')
graph.add_connection('A', 'B')
graph.add_connection('D', 'E')
graph.add_connection('E', 'A')
graph.add_connection('A', 'E')

print(graph.get_all_neighbours_of_node('A'))

graph.remove_connection('B', 'A')

print(graph.get_all_neighbours_of_node('A'))

"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        vertices_to_visit = Queue()
        vertices_to_visit.enqueue(starting_vertex)

        vertices_already_visited = set()

        while vertices_to_visit.size() > 0:

            current_vertex = vertices_to_visit.dequeue()

            if current_vertex not in vertices_already_visited:
                print(current_vertex)

                vertices_already_visited.add(current_vertex)

                for neighbor in self.get_neighbors(current_vertex):
                    vertices_to_visit.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        vertices_to_visit = Stack()
        vertices_to_visit.push(starting_vertex)

        vertices_already_visited = set()

        while vertices_to_visit.size() > 0:

            current_vertex = vertices_to_visit.pop()
            if current_vertex not in vertices_already_visited:
                print(current_vertex)
                vertices_already_visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    vertices_to_visit.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """

        def dft_helper(starting_vertex):

            if starting_vertex not in vertices_already_visited:
                print(starting_vertex)
                vertices_already_visited.add(starting_vertex)
                for neighbor in self.get_neighbors(starting_vertex):
                    dft_helper(neighbor)
       
        vertices_already_visited = set()
        dft_helper(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            # print(path)
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for next_vert in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            path = s.pop()
            # print(path)
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for next_vert in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(next_vert)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        path = []
        visited = set()

        def dfs_helper(start, end, visited, path):

            visited.add(start)
            path = path + [start]
            
            if start == end:
                return path

            for neighbor in self.get_neighbors(start):
                if neighbor not in visited:
                    new_path = dfs_helper(neighbor, destination_vertex, visited, path)
                    if new_path is not None:
                        return new_path
            return None

        return dfs_helper(starting_vertex, destination_vertex, visited, path)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
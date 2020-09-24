"""
If you can make a function to return the neighbor of this thing, you can treat the problem as s graph problem

If you can figure out when this item is and is not 'rekated' to other items, graphs
"""
"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # adjacency list
        # {vertex_id : set holding edges}
        # self.vertices = {A: set(B)}
        self.vertices = {}

        # adjacency matrix
        # more space efficient than adj. list if dense
        # self.vertices = [
        # #    a  b   c
        #     [0, 0, 0], # a
        #     [0, 0, 0], # b
        #     [0, 0, 0], # c
        # ]
        # self.vertices = []


    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # adjacency list time complexity: O(1)
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        else:
            return 

    # adjacency list time complexity: O(n)
    def delete_vertex(self, vertex_id):
        # delete the key-value pair
        # find/remove all references to this vertex
        for vert in self.vertices:
            # print(vert, self.vertices[vert])
            if vert == vertex_id:
                # print(vert)
                del self.vertices[vert]
                return self.delete_vertex(vertex_id)
            
        for vert in self.vertices:
            for edge in  self.vertices[vert]:
                # print('edge', edge)
                if edge == vertex_id:
                    # print('edge = vert_id', edge)
                    self.vertices[vert].remove(edge)
                    return self.delete_vertex(vertex_id)
                    # del edge

    

    # adjacency list time complexity: O(1)
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if (v1 or v2) not in self.vertices:
            print("vertex does not exist")
            return
        self.vertices[v1].add(v2)

    # adjacency list time complexity: O(1)
    def delete_edge(self, v1, v2):
        pass

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        for vert in self.vertices:
            if vert == vertex_id:
                return self.vertices[vert]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        to_print = []

        # while verts waiting in q
        while q.size() >0:
            curr_vert = q.dequeue()
            if curr_vert not in visited:
                visited.add(curr_vert)
                to_print.append(curr_vert)
                print(curr_vert)
                # print(self.get_neighbors(curr_vert))
                for neighbor in self.get_neighbors(curr_vert):
                    q.enqueue(neighbor)
        # print('bft', to_print)
        # print('bft', visited)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        to_print = []

        while stack.size()>0:
            curr_vert = stack.pop()
            if curr_vert not in visited:
                visited.add(curr_vert)
                to_print.append(curr_vert)
                print(curr_vert)
                for neighbor in self.get_neighbors(curr_vert):
                    stack.push(neighbor)


    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        print(starting_vertex)
        visited.add(starting_vertex)
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # queue holds path to starting_vertex
        queue = Queue()
        queue.enqueue([starting_vertex])

        visited = set()

        while queue.size() > 0:
            path = queue.dequeue()
            # grab last vertex from path
            curr_vert = path[-1]
            if curr_vert not in visited:
                if curr_vert == destination_vertex:
                    return path
                visited.add(curr_vert)
                
                for neighbor in self.get_neighbors(curr_vert):
                    # copy path and add neighbor
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()

        stack.push(starting_vertex)
        path= []

        while stack.size() > 0:
            curr_vert = stack.pop()
            curr_path = list(path + [curr_vert])
            if curr_vert == destination_vertex:
                return curr_path
            if curr_vert not in visited:
                visited.add(curr_vert)
                path.append(curr_vert)
                for neighbor in self.get_neighbors(curr_vert):
                    stack.push(neighbor)


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if len(path) == 0:
            path.append(starting_vertex)

        if starting_vertex == destination_vertex:
            return path
        visited.add(starting_vertex)
        neighbors = self.get_neighbors(starting_vertex)

        if len(neighbors) == 0:
            return None

        for neighbor in neighbors:
            if neighbor not in visited:
                # don't want to mutate original path so new_path
                new_path = path + [neighbor]
                result = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                if result is not None:
                    return  result


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
    # print(graph.get_neighbors(4))
    # print(graph.vertices)

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
    print('Valid BFS path: [1, 2, 4, 6] ')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('graph.dfs(1, 6)')
    print(graph.dfs(1, 6))
    print('graph.dfs_recursive(1, 6)')
    print(graph.dfs_recursive(1, 6))

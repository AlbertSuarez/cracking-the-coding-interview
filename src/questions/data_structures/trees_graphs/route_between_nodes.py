from queue import Queue

from src.helper.question import Question


class RouteBetweenNodes(Question):

    def solve(self):
        """
        Given a directed graph and two nodes (node_init and node_end),
        design an algorithm to find out whether there is a route from node_init to node_end.
        :return: O[n] - time | O[n] - space
        """
        graph: dict = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': [],
            'F': []
        }
        node_init = 'B'
        node_end = 'C'

        if node_init == node_end:
            self.result = True
            return
        visited = dict.fromkeys(graph.keys(), False)  # Initialized all as False
        queue = Queue()  # Our queue for searching as BFS
        queue.put(node_init)
        visited[node_init] = True
        while not queue.empty():
            front_queue = queue.get()
            if front_queue == node_end:
                self.result = True
                return
            for adj in graph[front_queue]:
                if not visited[adj]:
                    queue.put(adj)
                    visited[adj] = True
        self.result = False


if __name__ == '__main__':
    with RouteBetweenNodes(RouteBetweenNodes.__name__) as question_class:
        question_class.solve()

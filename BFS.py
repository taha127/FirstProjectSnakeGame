from collections import deque
from Utility import Node
from Algorithm import Algorithm


class BFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake):
        # start clean
        self.frontier = deque([])
        self.explored_set = []
        self.path = []

        initialstate, goalstate = self.get_initstate_and_goalstate(snake)

        # open list
        self.frontier.append(initialstate)

        # while we have states in open list
        while len(self.frontier) > 0:
            current_node = self.frontier.popleft()

            if current_node.equal(goalstate):
                return self.get_path(current_node)

            neighbors = self.get_neighbors(current_node)
            for neighbor in neighbors:
                if (neighbor not in self.explored_set and not self.inside_body(snake, neighbor)
                        and not self.outside_boundary(neighbor)):
                    neighbor.parent = current_node
                    self.frontier.append(neighbor)
                    self.explored_set.append(neighbor)
        return None

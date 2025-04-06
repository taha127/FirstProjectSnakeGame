from Utility import Node
from Algorithm import Algorithm


class DFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def recursive_DFS(self, snake, goalstate, currentstate):
        # your code ----------------------------------------------------------------------

        return None

    def run_algorithm(self, snake):
        # to avoid looping in the same location
        if len(self.path) != 0:
            # while you have path keep going
            path = self.path.pop()

            if self.inside_body(snake, path):
                self.path = [] # or calculate new path!
            else:
                return path

        # start clean
        self.frontier = []
        self.explored_set = []
        self.path = []

        initialstate, goalstate = self.get_initstate_and_goalstate(snake)

        self.frontier.append(initialstate)

        # return path
        return self.recursive_DFS(snake, goalstate, initialstate)

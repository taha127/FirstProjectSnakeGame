from Utility import Node
from Algorithm import Algorithm


class DFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def recursive_DFS(self, snake, goalstate, currentstate):
        if (currentstate.x, currentstate.y) == (goalstate.x, goalstate.y):
            self.path.append(currentstate)
            return currentstate

        self.explored_set.add((currentstate.x, currentstate.y))

        for neighbor in self.get_neighbors(currentstate):
            if (neighbor.x, neighbor.y) not in self.explored_set and \
                    not self.outside_boundary(neighbor) and \
                    not self.inside_body(snake, neighbor):
                next_step = self.recursive_DFS(snake, goalstate, neighbor)
                if next_step:
                    if currentstate != self.initial_state:
                        self.path.append(currentstate)
                        return currentstate
                    self.path.pop()
                    return next_step
        return None

    def run_algorithm(self, snake):
        # to avoid looping in the same location
        if len(self.path) != 0:
            # while you have path keep going
            next_step = self.path.pop()

            if self.inside_body(snake, next_step):
                self.path = []  # or calculate new path!
            else:
                return next_step

            # start clean
        self.frontier = []
        self.explored_set = set()
        self.path = []
        self.initial_state, goal_state = self.get_initstate_and_goalstate(snake)

        # return path
        ns = self.recursive_DFS(snake, goal_state, self.initial_state)
        return ns

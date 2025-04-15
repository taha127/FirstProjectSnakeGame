from Algorithm import Algorithm


class A_STAR(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake):
        # clear everything
        self.frontier = []
        self.explored_set = []
        self.path = []
        initialstate, goalstate = self.get_initstate_and_goalstate(snake)
        initialstate.g = 0
        initialstate.h = self.manhattan_distance(initialstate, goalstate)
        initialstate.f = initialstate.g + initialstate.h
        self.frontier.append(initialstate)
        while len(self.frontier) > 0:
            current_node = min(self.frontier, key=lambda x: x.f)
            self.frontier.remove(current_node)
            if current_node.x == goalstate.x and current_node.y == goalstate.y:
                return self.get_path(current_node)
            self.explored_set.append(current_node)
            for neighbor in self.get_neighbors(current_node):
                if (neighbor in self.explored_set or
                        self.inside_body(snake, neighbor) or
                        self.outside_boundary(neighbor)):
                    continue
                tentative_g = current_node.g + 1
                if neighbor not in self.frontier or tentative_g < neighbor.g:
                    neighbor.parent = current_node
                    neighbor.g = tentative_g
                    neighbor.h = self.manhattan_distance(neighbor, goalstate)
                    neighbor.f = neighbor.g + neighbor.h
                    if neighbor not in self.frontier:
                        self.frontier.append(neighbor)
        return None

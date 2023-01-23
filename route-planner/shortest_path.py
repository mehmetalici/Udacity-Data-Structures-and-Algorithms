import numpy as np
import copy

class _Node:
    def __init__(self, id, x, y, is_goal=False, is_start=False):
        self.is_goal = is_goal
        self.is_start = is_start
        self.id = id
        self.x = x
        self.y = y
        
    def __sub__(self, other):
        return [self.x - other.x, self.y - other.y]

    
class _Path:
    def __init__(self, starting_node=None):
        self.nodes = []
        if starting_node is not None:
            self.nodes.append(starting_node)
        self.cost = 0
        self.is_blocked = False

    def _append(self, new):
        return self.nodes.append(new)

    def peek(self):
        return self.nodes[-1]

    def add_intersection(self, intersection, cost, in_place=True):
        path = self if in_place else self.copy()

        path._append(intersection)
        if cost == 0:
            path.is_reached = True
        path.cost += cost

        return None if in_place else path

    def copy(self):
        return copy.deepcopy(self)
    

class _ShortestPath:
    def __init__(self, m):
        self.map = m
        self.nodes = []
        self.roads = []
        self.paths = []

    def _populate_nodes_by_map(self):
        self.nodes = [None] * len(self.map.intersections)
        for idx, point in self.map.intersections.items():
            self.nodes[idx] = _Node(id=idx, x=point[0], y=point[1])

    def _populate_roads_by_map(self):
        # Init roads
        self.roads = []
        for adjacent_node_indices in self.map.roads:
            self.roads.append([self.nodes[adjacent_node_idx] for adjacent_node_idx in adjacent_node_indices])

    def _expand(self, intersection: int, blacklist: list) -> list:
        new_frontiers = []
        for adjacent_node in self.roads[intersection]:
            if not any([adjacent_node.is_start, adjacent_node.id in blacklist]):
                new_frontiers.append(adjacent_node.id)            
        return new_frontiers
    
    def _calculate_step_cost(self, current_isec: int, next_isec: int, goal: int):
        g = self.distance(current_isec, next_isec)
        h = self.distance(next_isec, goal)
        f = g + h
        return f

    def _get_path_by_last_intersection(self, isec_current: int):               
        for path in self.paths:
            if path.peek() == isec_current:
                return path
        raise PathNotFoundError

    def _get_min_cost_path(self):
        return min(self.paths, key=lambda path: path.cost)


    def shortest_path(self, start: int, goal: int):
        if start == goal:
            return [start]

        # Clean-up for the current session
        self._populate_nodes_by_map()
        self._populate_roads_by_map()
        self.nodes[goal].is_goal = True
        self.nodes[start].is_start = True

        # Init
        frontiers = set()
        first_path = _Path(start)
        self.paths.append(first_path)
        frontiers.add(start)
        new_frontiers = self._expand(start, blacklist=first_path.nodes)
        shortest_path = None
        shortest_path_hist = []
        # Main Loop
        current_intersection = start
        while True:
            frontiers.remove(current_intersection)
            path_to_frontiers = self._get_path_by_last_intersection(current_intersection)
            self.paths.remove(path_to_frontiers)
            for new_frontier in new_frontiers:
                step_cost = self._calculate_step_cost(current_intersection, new_frontier, goal)
                path_with_frontier = path_to_frontiers.add_intersection(new_frontier, step_cost, in_place=False)
                if new_frontier in frontiers:
                    # Resolve frontier crash
                    previous_path = self._get_path_by_last_intersection(new_frontier)
                    if previous_path.nodes == [8, 14, 16, 37, 12, 17, 10]:
                        print("Please put a breakpoint here.")
                    if previous_path.cost >= path_with_frontier.cost:
                        self.paths.remove(previous_path)
                        self.paths.append(path_with_frontier)
                else:
                    self.paths.append(path_with_frontier)
            if len(self.paths) == 0:
                break
            current_path = self._get_min_cost_path()
            current_intersection = self._get_min_cost_path().peek()
            if current_intersection == goal:
                if shortest_path is None:
                    shortest_path = current_path
                shortest_path = current_path if shortest_path.cost > current_path.cost else shortest_path
                shortest_path_hist.append(shortest_path)
            frontiers.update(new_frontiers)
            new_frontiers = self._expand(current_intersection, blacklist=current_path.nodes)
            
        return shortest_path.nodes


    def distance(self, isec_1: int, isec_2: int):
        return np.linalg.norm(self.nodes[isec_1] - self.nodes[isec_2])
    

class PathNotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def shortest_path(m, start: int, goal: int):
    sp = _ShortestPath(m)
    return sp.shortest_path(start, goal)
    
    
    
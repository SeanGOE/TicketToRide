from math import sqrt
import sys
from typing import Dict, List, Set, Tuple
from priority_queue import PriorityQueue

# You do not need to change this class.  It is used as the return type for get_minimum_path
class RouteInfo:
    def __init__(self, 
                 route: List[Tuple[str, str]], # list of tuples of friendly names for the start and destination cities
                 route_ids: List[Tuple[int, int]], # list of tuples of ids for the start and destination cities
                 cost: int) -> None: # the total cost of the route from start to destination
        self.route = route
        self.route_ids = route_ids
        self.cost = cost

class Edge:
    def __init__(self, start, finish, weight) -> None:
        self.start = start
        self.finish = finish
        self.weight = weight

# TODO: Implement the methods on the PathFinder class using an underlying graph representation
# of your choice. Feel free to use your graph classes from the practice exercises; copy the appropriate
# files into your project and import the classes at the top of this file.
class PathFinder:
    def __init__(self) -> None:
        self.nodes:Dict[Set] = dict()

    # TODO: adds an edge to the graph, using a the id of the start node and id of the finish node
    def add_edge(self, start_id: int, finish_id:int , cost: float) -> None:
        new_edge = Edge(start_id, finish_id, cost)
        self.nodes[start_id].add(new_edge)

    # TODO: adds a node to the graph, passing in the id, friendly name, and location of the node.
    # location is a tuple with the x and y coordinates of the location
    def add_node(self, id: int, name: str, location: Tuple[float, float]) -> None:
        self.nodes.setdefault(name, set())

    # TODO: calculates the minimum path using the id of the start city and id of the destination city, using A*
    # Returns a RouteInfo object that contains the edges for the route.  See RouteInfo above for attributes
    # Note: This implementation should use A*.  Tests that should pass 
    def get_minimum_path(self, start_city_id: int, destination_id:int ) -> RouteInfo:
        pri_queue = PriorityQueue()
        for edge in self.nodes:
            pass
        start = RouteInfo()
        pri_queue.enqueue()

    def get_min_path_recursive(self, location, destination):
        pass

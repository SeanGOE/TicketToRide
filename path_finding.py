from math import sqrt
import sys
from typing import Dict, List, Set, Tuple
from priority_queue import PriorityQueue
import L2_adjacency_list_graph
from L2_adjacency_list_graph import AdjacencyListGraph


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
    def __init__(self, is_directed = True) -> None:
        self.graph = AdjacencyListGraph(is_directed)
        self.ids_to_name = {}
        self.name_to_ids = {}

        self.map_data = {}
        self.previous_nodes = {}

    # TODO: adds an edge to the graph, using a the id of the start node and id of the finish node
    def add_edge(self, start_id: int, finish_id:int , cost: float) -> None:
        self.graph.add_edge(start_id, finish_id, cost)

    # TODO: adds a node to the graph, passing in the id, friendly name, and location of the node.
    # location is a tuple with the x and y coordinates of the location
    def add_node(self, id: int, name: str, location: Tuple[float, float]) -> None:
        self.graph.add_node(id)
        self.ids_to_name[id] = (name, location)
        self.name_to_ids[name] = (id, location)

    # TODO: calculates the minimum path using the id of the start city and id of the destination city, using A*
    # Returns a RouteInfo object that contains the edges for the route.  See RouteInfo above for attributes
    # Note: This implementation should use A*.  Tests that should pass 
    def get_minimum_path(self, start_city_id: int, destination_id:int ) -> RouteInfo:
        
        pri_queue = PriorityQueue()
        pri_queue.enqueue(0, [start_city_id])

        visited = set()
        visited.add(start_city_id)

        self.map_data[start_city_id] = 0
        self.previous_nodes[start_city_id] = start_city_id

        while pri_queue.size() > 0:
            route = pri_queue.dequeue()
            
            for nodes in self.graph.nodes[route[len(visited) - 1]]:

                # visited.add(nodes.start)
                if nodes.finish not in visited:

                    start_coords = self.ids_to_name[nodes.start][1]
                    finish_coords = self.ids_to_name[nodes.finish][1]
                    potential_cost = sqrt(pow((start_coords[0] - finish_coords[0]), 2) + pow((start_coords[1] - finish_coords[1]), 2)) + nodes.weight
                    
                    new_cost = self.map_data[nodes.start] + nodes.weight
                    
                    if self.map_data[nodes.finish] > new_cost:
                        self.map_data[nodes.finish] = new_cost
                        self.previous_nodes[nodes.finish] = nodes.start
                    
                    # new_route = route[:]
                    # new_route.append(nodes.finish)

                    if nodes.finish == destination_id:
                        # return self.route_decoder(new_route)
                        return self.route_decoder()
                    pri_queue.enqueue(potential_cost + self.map_data[nodes.start], nodes.finish)

            #visited.add(nodes.start)

    def route_decoder(self, route: List):
        cost = 0
        route_names = []
        route_ids = []
        for start in range(len(route) - 1):
            for finish in range(start + 1, len(route)):
                for nodes in self.graph.nodes[route[start]]:
                    if nodes.finish == route[finish]:
                        cost += nodes.weight
                        route_names.append((self.ids_to_name[route[start]][0], self.ids_to_name[route[finish]][0]))
                        route_ids.append((route[start], route[finish]))
                        break
        route_info = RouteInfo(route_names, route_ids, cost)
        return route_info
                    


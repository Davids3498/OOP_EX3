from src.GraphInterface import GraphInterface
import heapq


class DiGraph(GraphInterface):
    def __init__(self):
        self.V = {}
        self.E_num = 0
        self.MC = 0

    def __repr__(self):
        return "Graph: |V|=" + len(self.V).__str__() + " , |E|=" + self.E_num.__str__()

    """
    :returns the number of nodes in the graph
    """

    def v_size(self) -> int:
        return len(self.V)

    """
    :returns the number of edges in the graph
    """

    def e_size(self) -> int:
        return self.E_num

    """
    :returns a dictionary of all the nodes in the graph
    """

    def get_all_v(self) -> dict:
        return self.V

    """
    :returns a dictionary of all the nodes that this node is pointing to
    """

    def all_in_edges_of_node(self, id1: int) -> dict:
        if self.V.__contains__(id1):
            return self.V[id1].get_in()

    """
    :returns a dictionary of all the nodes that are pointing to this node
    """

    def all_out_edges_of_node(self, id1: int) -> dict:
        if self.V.__contains__(id1):
            return self.V[id1].get_out()

    """
    :returns the number of changes are made in this graph
    """

    def get_mc(self) -> int:
        return self.MC

    """
    adds an edge between two nodes 
    """

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.V or id2 not in self.V or id2 in self.V[id1].get_out() or weight < 0:
            return False
        else:
            self.V[id1].add_out(id2, weight)
            self.V[id2].add_in(id1, weight)
            self.E_num += 1
            self.MC += 1
            return True

    """
    adds a node to the graph 
    """

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if not (self.V.__contains__(node_id)):
            n = Node(node_id, pos)
            self.V[node_id] = n
            self.MC += 1
            return True
        else:
            return False

    """
    removes a node from the graph 
    """

    def remove_node(self, node_id: int) -> bool:
        if not (self.V.__contains__(node_id)):
            return False
        else:
            get_in_copy = self.V[node_id].get_in().copy()
            self.MC -= len(self.V[node_id].get_in())
            for node in get_in_copy.keys():
                self.remove_edge(node, node_id)
            self.E_num -= len(self.V[node_id].get_out())
            self.V.pop(node_id)
            self.MC += 1
            return True

    """
    removes the edge between two nodes 
    """

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self.V or node_id2 not in self.V or node_id2 not in self.V[node_id1].get_out():
            return False
        else:
            del self.V[node_id1].get_out()[node_id2]
            del self.V[node_id2].get_in()[node_id1]
            self.E_num -= 1
            self.MC += 1
            return True

    """
    Node class
    """


class Node(object):
    def __init__(self, num: int, pos: tuple):
        self.id = num
        self.Out = {}  # from this node to other nodes
        self.In = {}  # from other nodes to this node
        self.distance = "inf"
        self.previous_node = None
        self.pos = pos

    def add_out(self, nei: int, w: float):
        self.Out[nei] = w

    def add_in(self, nei: int, w: float):
        self.In[nei] = w

    def get_out(self):
        return self.Out

    def get_in(self):
        return self.In

    def get_id(self):
        return self.id

    def get_previous_node(self):
        return self.previous_node

    def set_previous_node(self, node):
        self.previous_node = node

    def get_distance(self):
        return self.distance

    def set_distance(self, dist: float):
        self.distance = dist

    def get_weight(self, nei):
        return self.Out[nei]

    def get_node(self):
        return self

    def get_pos(self):
        return self.pos

    def set_pos(self, pos: tuple):
        self.pos = pos

    def __repr__(self):
        return "|edges out| " + self.Out.__str__() + " |edges in| " + self.In.__str__()

    def __lt__(self, other):
        if self.get_distance() == "inf" and other.get_distance() == "inf":
            return 0
        if self.get_distance() == "visited" and other.get_distance() == "visited":
            return 0
        if self.get_distance() == "inf":
            return -1
        if other.get_distance() == "inf":
            return 1
        return self.get_distance() < other.get_distance()

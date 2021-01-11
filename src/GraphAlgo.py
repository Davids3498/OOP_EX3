import json
from typing import List
import heapq
import matplotlib.pyplot as plt
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
import random


class GraphAlgo(GraphAlgoInterface, DiGraph):
    def __init__(self, g: DiGraph = None):
        self.g = g

    def get_graph(self):
        return self.g

    def load_from_json(self, file_name: str) -> bool:
        self.g = DiGraph()
        try:
            with open(file_name, "r") as file:
                jsondict = json.load(file)
                for node in jsondict["Nodes"]:
                    if "pos" in node:
                        i = 0
                        pos = ()
                        for position in node["pos"].split(','):
                            pos = pos + (float(position),)
                        self.g.add_node(node_id=node["id"], pos=pos)
                    else:
                        self.g.add_node(node_id=node["id"])
                for edge in jsondict["Edges"]:
                    self.g.add_edge(id1=edge["src"], id2=edge["dest"], weight=edge["w"])
            return True
        except IOError as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        Nodes = []
        Edges = []

        for node in self.g.get_all_v():
            if self.g.get_all_v()[node].get_pos() is not None:
                pos = str(self.g.get_all_v()[node].get_pos())
                Nodes.append({"id": node, "pos": pos})
            else:
                Nodes.append({"id": node})
            for edge in self.g.all_out_edges_of_node(node):
                Edges.append({"src": node, "dest": edge, "w": self.g.get_all_v()[node].get_weight(edge)})
        jsondict = {"Nodes": Nodes, "Edges": Edges}

        try:
            with open(file_name, "w") as file:
                json.dump(jsondict, fp=file)
                return True
        except IOError as e:
            print(e)
            return False
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        for node in self.g.get_all_v():
            self.g.get_all_v()[node].set_distance("inf")
            self.g.get_all_v()[node].set_previous_node(None)

        if id1 not in self.g.get_all_v() or id2 not in self.g.get_all_v():
            return (float('inf'), [])
        dist = 0
        self.g.get_all_v()[id1].set_distance(dist)
        PQ = []
        heapq.heappush(PQ, self.g.get_all_v()[id1])

        while len(PQ):
            node1 = heapq.heappop(PQ)
            dist = self.g.get_all_v()[node1.get_id()].get_distance()  # equals to: dist = node1.get_distance()
            for node2 in self.g.all_out_edges_of_node(node1.get_id()):
                if self.g.get_all_v()[node2].get_distance() == "inf" or self.g.get_all_v()[node2].get_distance() > dist:
                    heapq.heappush(PQ, self.g.get_all_v()[node2])
                new_dist = dist + self.g.get_all_v()[node1.get_id()].get_weight(node2)
                if self.g.get_all_v()[node2].get_distance() == "inf" or new_dist < self.g.get_all_v()[
                    node2].get_distance():
                    self.g.get_all_v()[node2].set_distance(new_dist)
                    self.g.get_all_v()[node2].set_previous_node(node1)

        if self.g.get_all_v()[id2].get_distance() == "inf":
            return (float('inf'), [])
        else:
            L = []
            L.insert(0, id2)
            _id = self.g.get_all_v()[id2].get_previous_node()
            while _id != None:
                L.insert(0, _id.get_id())
                _id = self.g.get_all_v()[_id.get_id()].get_previous_node()
            return (self.g.get_all_v()[id2].get_distance(), L)

    def connected_component(self, id1: int) -> list:
        for node in self.g.get_all_v():
            self.g.get_all_v()[node].set_distance("inf")

        L_out = []
        L_in = []
        PQ = []

        heapq.heappush(PQ, self.g.get_all_v()[id1])
        self.g.get_all_v()[id1].set_distance("visited")
        while len(PQ):
            node1 = heapq.heappop(PQ)
            L_out.insert(0, node1.get_id())
            for node2 in self.g.all_out_edges_of_node(node1.get_id()):
                if self.g.get_all_v()[node2].get_distance() == "inf":
                    self.g.get_all_v()[node2].set_distance("visited")
                    heapq.heappush(PQ, self.g.get_all_v()[node2])

        for i in L_out:
            self.g.get_all_v()[i].set_distance("inf")

        heapq.heappush(PQ, self.g.get_all_v()[id1])
        self.g.get_all_v()[id1].set_distance("visited")
        while len(PQ):
            node1 = heapq.heappop(PQ)
            L_in.insert(0, node1.get_id())
            for node2 in self.g.all_in_edges_of_node(node1.get_id()):
                if self.g.get_all_v()[node2].get_distance() == "inf":
                    self.g.get_all_v()[node2].set_distance("visited")
                    heapq.heappush(PQ, self.g.get_all_v()[node2])

        return list(set(L_out) & set(L_in))

    def connected_components(self) -> List[list]:
        visited = []
        ans = []

        for i in self.g.get_all_v():
            if i not in visited:
                L = self.connected_component(i)
                ans.append(L)
                visited.extend(L)

        return ans

    def plot_graph(self) -> None:
        x_val = []
        y_val = []

        for node in self.g.get_all_v():
            if self.g.get_all_v()[node].get_pos() == None:
                pos = ()
                for i in range(2):
                    pos = pos + (random.random(),)
                pos = pos + (0,)
                self.g.get_all_v()[node].set_pos(pos)

        ax = plt.axes()

        for node1 in self.g.get_all_v():
            startX = self.g.get_all_v()[node1].get_pos()[0]
            startY = self.g.get_all_v()[node1].get_pos()[1]
            plt.annotate(node1, xy=(startX, startY), fontsize=12, color="green")
            x_val.append(self.g.get_all_v()[node1].get_pos()[0])
            y_val.append(self.g.get_all_v()[node1].get_pos()[1])
            for node2 in self.g.all_out_edges_of_node(node1):
                endX = self.g.get_all_v()[node2].get_pos()[0]
                endY = self.g.get_all_v()[node2].get_pos()[1]
                ax.annotate("", xy=(startX, startY), xytext=(endX, endY), arrowprops=dict(arrowstyle="->"))

        plt.title("Graph")
        plt.plot(x_val, y_val, 'ro')
        plt.show()

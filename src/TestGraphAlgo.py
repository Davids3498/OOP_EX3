import unittest
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


def Graph_gen(n):
    g: DiGraph = DiGraph()
    for i in range(n):
        g.add_node(i)
        if i != 0:
            g.add_edge(i - 1, i, i)
    return g


class TestGraphAlgo(unittest.TestCase):
    def test_get_graph(self):
        g = Graph_gen(5)
        g_algo = GraphAlgo(g)
        self.assertEqual(g_algo.get_graph(), g)

    def test_load_save(self):
        g = Graph_gen(5)
        g_algo = GraphAlgo(g)
        file = "../TestSave.json"
        g_algo.save_to_json(file)
        new_algo = GraphAlgo()
        self.assertEqual(new_algo.load_from_json(file), True)
        for i in range(5):
            self.assertEqual(new_algo.get_graph().all_in_edges_of_node(i), g.all_in_edges_of_node(i))
            self.assertEqual(new_algo.get_graph().all_out_edges_of_node(i), g.all_out_edges_of_node(i))

    def test_shortest_path(self):
        g = Graph_gen(5)
        g.add_edge(0, 4, 100)
        sp = (10, [0, 1, 2, 3, 4])
        g_algo = GraphAlgo(g)
        spa = g_algo.shortest_path(0, 4)
        self.assertEqual(sp, spa)
        sp = (float('inf'), [])
        spa = g_algo.shortest_path(4, 0)
        self.assertEqual(sp, spa)
        self.assertEqual(sp, spa)

    def test_connected_component(self):
        g = Graph_gen(5)
        g_algo = GraphAlgo(g)
        self.assertEqual(g_algo.connected_component(0), [0])
        self.assertEqual(g_algo.connected_component(1), [1])
        self.assertEqual(g_algo.connected_component(2), [2])
        self.assertEqual(g_algo.connected_component(3), [3])
        self.assertEqual(g_algo.connected_component(4), [4])
        for i in range(1, 5):
            g.add_edge(i, i - 1, i)
        self.assertEqual(g_algo.connected_component(0), [0, 1, 2, 3, 4])

    def test_connected_components(self):
        g = Graph_gen(5)
        g_algo = GraphAlgo(g)
        self.assertEqual(g_algo.connected_components(), [[0], [1], [2], [3], [4]])
        g.add_edge(4, 0, 1)
        self.assertEqual(g_algo.connected_components(), [[0, 1, 2, 3, 4]])


if __name__ == '__main__':
    unittest.main()

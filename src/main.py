from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo

def check():

    check0()



def check0():
    """
       This function tests the naming (main methods of the GraphAlgo class, as defined in GraphAlgoInterface.
    :return:
    """
    g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
    file = "../data/A5"
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    g_algo.plot_graph()


if __name__ == '__main__':
    check()
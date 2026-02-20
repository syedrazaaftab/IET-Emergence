import networkx as nx
import numpy as np

def generate_ensemble(ensemble_type, N, seed=None):
    """
    Generate graph from one of 4 ensembles used in the paper.
    - ER: Erdős–Rényi (sparse p=3/N)
    - BA: Barabási–Albert (scale-free)
    - WS: Watts–Strogatz (small-world)
    - RR: Random regular (degree 3)
    """
    if seed is not None:
        np.random.seed(seed)
    
    N = int(N)
    if ensemble_type == "ER":
        return nx.erdos_renyi_graph(N, 3.0 / N)
    elif ensemble_type == "BA":
        return nx.barabasi_albert_graph(N, 2)
    elif ensemble_type == "WS":
        return nx.watts_strogatz_graph(N, 4, 0.1)
    elif ensemble_type == "RR":
        return nx.random_regular_graph(3, N)
    else:
        raise ValueError(f"Unknown ensemble: {ensemble_type}")

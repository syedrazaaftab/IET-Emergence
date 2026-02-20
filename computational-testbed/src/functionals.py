import networkx as nx
import numpy as np

def complexity_functional(G, w1=1.0, w2=1.0, w3=1.0):
    """
    Computes C(G) = w1*Δλ - w2*Var(σ) + w3*κ_G
    Includes weight sensitivity (w1, w2, w3) for the analysis in the paper.
    """
    A = nx.adjacency_matrix(G).todense()
    
    # Spectral gap Δλ
    ev = np.linalg.eigvalsh(A)
    delta_lambda = ev[-1] - ev[-2]
    
    # Singular-value variance Var(σ)
    s = np.linalg.svd(A, compute_uv=False)
    var_sigma = np.var(s)
    
    # Ollivier-Ricci placeholder (can be expanded later)
    kappa_G = 0.0  # TODO: replace with real Ollivier-Ricci average
    
    return w1 * delta_lambda - w2 * var_sigma + w3 * kappa_G

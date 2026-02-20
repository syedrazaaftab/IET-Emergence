import numpy as np
from src.graph_generation import generate_ensemble
from src.functionals import complexity_functional

print("Stability test under random edge flips (placeholder)")

N = 200
G = generate_ensemble("ER", N, seed=42)
original_C = complexity_functional(G)

# Simulate 50 random edge flips and check δC
stable_count = 0
for i in range(50):
    G_copy = G.copy()
    # Random edge flip (add or remove)
    u, v = np.random.choice(list(G_copy.nodes()), 2, replace=False)
    if G_copy.has_edge(u, v):
        G_copy.remove_edge(u, v)
    else:
        G_copy.add_edge(u, v)
    
    new_C = complexity_functional(G_copy)
    delta_C = abs(new_C - original_C)
    if delta_C < 0.01:
        stable_count += 1

print(f"Fraction of stable flips: {stable_count/50:.3f}")
print("✅ Stability test complete (expand later with full statistics)")

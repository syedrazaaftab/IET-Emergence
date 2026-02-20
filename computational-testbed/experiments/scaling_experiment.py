import numpy as np
import matplotlib.pyplot as plt
from src.graph_generation import generate_ensemble
from src.functionals import complexity_functional

# Parameters from the paper
Ns = np.array([50, 100, 200, 400, 800])
ensembles = ["ER", "BA", "WS", "RR"]
num_runs = 20                     # for error bars
weights_list = [(1.0,1.0,1.0), (1.5,0.5,1.0), (0.5,1.5,1.0)]  # sensitivity analysis

results = {}

print("Running scaling experiment with error bars + weight sensitivity...")

for ens in ensembles:
    means = []
    stds = []
    for N in Ns:
        all_vals = []
        for w in weights_list:
            for run in range(num_runs):
                G = generate_ensemble(ens, N, seed=run)
                val = complexity_functional(G, *w)
                all_vals.append(val)
        means.append(np.mean(all_vals))
        stds.append(np.std(all_vals))
    results[ens] = (means, stds)
    print(f"  {ens} done.")

# Save plot with error bars (this will be Figure 1 in the paper)
plt.figure(figsize=(8, 5))
for ens in ensembles:
    plt.errorbar(Ns, results[ens][0], yerr=results[ens][1], 
                 label=ens, capsize=4, linewidth=2)
plt.xscale('log')
plt.xlabel('Graph size N')
plt.ylabel('Mean C(G) ± std')
plt.title('Scaling of C(G) across ensembles\n(with weight sensitivity and error bars)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('plots/scaling_with_errorbars.png', dpi=300)
plt.show()

print("✅ Plot saved as plots/scaling_with_errorbars.png")
print("Ready for the paper!")

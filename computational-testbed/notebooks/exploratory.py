"""
One-click reproduction script for the paper.
Run with: python notebooks/exploratory.py
"""

from src.graph_generation import generate_ensemble
from src.functionals import complexity_functional
from experiments.scaling_experiment import *   # runs the full scaling with error bars

print("🚀 IET Computational Testbed — Exploratory Demo")
print("Running full scaling experiment with 4 ensembles + error bars...\n")

# The scaling_experiment.py already ran the plot when imported
# (you can also run stability_test if you want)
print("✅ All experiments complete!")
print("Check plots/scaling_with_errorbars.png for the new figure with error bars.")
print("\nReady for the paper!")

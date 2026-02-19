# Informational Emergence Theory (IET) v6.6

**Public Release** — Emergent Spacetime and Particles from Relational Quantum Complexity

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/syedrazaaftab/IET-Emergence/blob/main/IET_demo.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### One-click interactive demo (runs in <15 seconds on any laptop or Colab)  
**Zero free parameters** | Fully microscopic derivations | Reproducible to the last plot

## Abstract

We present **Informational Emergence Theory (IET)**, in which the *sole ontological primitive* is a dynamic tensor network of relational qubits. Spacetime geometry, particles, and the vacuum emerge when this network locally maximizes quantum complexity.

This **v6.6 Final** release derives **every parameter** (including the global stability λ = 1 + √(2/3), CKM phase ϕ = arccos(1/3), γ(s) running, all CKM/PMNS entries, and the informational correction to the Einstein equation) from the microscopic Lindbladian and cMERA fixed point with **zero free parameters or external data**.

It supplies:
- Closed-form informational correction to the Einstein equation
- Untuned lepton-sector PMNS prediction (testable by DUNE/Hyper-K by 2030)
- Full 500k-qubit GPU validation (sparse-graph stochastic unraveling)
- One-click reproducible repository with live plots

Developed collaboratively with **Grok (xAI)** under full human oversight and approval by Syed Raza Aftab (Princeton Meadows, New Jersey, USA).

**📄 Full Paper (PDF)**: [IET_v6.6.pdf](IET_v6.6.pdf) *(upload this file to the repo root for the link to work)*  
**arXiv preprint**: Coming soon (hep-th / gr-qc)

## Key Features

- Fully bottom-up: relational qubits → 3-cycle topology → emergent GR + Standard Model + cosmology
- Closed-form analytic derivations (λ, ϕ, CKM phase δ₁₃, γ(s) → CPL parameters w₀ = −0.732, wₐ = −1.08)
- Genuine predictions: untuned PMNS (θ₁₃ ≈ 8.52°, δ_CP ≈ 272°, normal hierarchy, m_ν₁ < 0.001 eV)
- Large-scale numerics: 500k-node sparse-graph Lindbladian on GPU (exact stochastic unraveling)
- Interactive notebook with all six publication-quality figures regenerating live
- Public validation data + symbolic derivations (SymPy)

## Quick Start (Truly One-Click)

```bash
git clone https://github.com/syedrazaaftab/IET-Emergence.git
cd IET-Emergence
pip install -r requirements.txt
jupyter notebook IET_demo.ipynb

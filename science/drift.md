# Sensitivity to within-block drift

The [common-filter coding theorem](capacity.md) uses one unknown polarization filter per known block. Here each slot can have its own filter, within a prescribed distance of some admissible common filter.

Suppose the actual filter in slot $`i`$ is a contraction $`A_i`$ with $`\lVert A_i-A\rVert_\infty\le\epsilon_i`$ for one admissible block filter $`A`$. A separate global phase in each slot can be ignored when measuring this distance. The norm below is the full diamond norm. Expanding the difference of the two surviving maps on an input with a reference gives

```math
\lVert A_i(\cdot)A_i^\dagger-A(\cdot)A^\dagger\rVert_\diamond
 \le 2\epsilon_i .
```

The difference of the erasure maps is the scalar functional with Hermitian coefficient $`A^\dagger A-A_i^\dagger A_i`$, whose diamond norm is its operator norm, again at most $`2\epsilon_i`$. Summing gives $`\lVert \Gamma_{A_i}-\Gamma_A\rVert_\diamond\le4\epsilon_i`$. Tensor-product telescoping, followed by the fixed encoder and receiver operation, bounds the error for one block by

```math
\lVert \widetilde\Phi_n-\Phi_n\rVert_\diamond
 \le \min\!\left\{2,\ 4\sum_{i=1}^n\epsilon_i\right\}.
```

The notation refers to even $`n`$ here, or to the corresponding ignored-slot construction at odd $`n`$. For a fixed finite-horizon outer code the total diamond perturbation is at most the sum of its block bounds. In particular, its entanglement fidelity, taken as the overlap with the target state, decreases by at most half that bound.

A fixed positive drift tolerance is also possible at fixed $`n\ge4`$ and $`x+y>1`$. Choose a finite inner code spanning $`L`$ ideal blocks that transmits one qubit with diamond error at most $`\eta/2`$. Positive ideal capacity guarantees such a code, by restricting strong subspace transmission to a single qubit and using fixed-dimensional channel norm equivalence. If every slot has deviation at most $`\eta/(8nL)`$, the induced one-qubit channel of each $`L`$-block group differs from identity by at most $`\eta`$, uniformly in its axis sequence and drift.

Across $`N`$ such groups, choose a positive-rate quantum code correcting all errors on at most $`\lfloor\alpha N\rfloor`$ qubits, for some constant $`\alpha>0`$. Asymptotically good stabilizer codes supply such a family. For a fixed drift sequence the induced channel is $`\bigotimes_{j=1}^N(\mathrm{id}+\Delta_j)`$, with $`\lVert \Delta_j\rVert_\diamond\le\eta`$. Expand the tensor product. After encoding and recovery, all terms of weight between one and $`\lfloor\alpha N\rfloor`$ vanish because each $`\Delta_j`$ is a difference of two channels and every corresponding pattern of channel errors is corrected exactly. The residual diamond error satisfies

```math
\sum_{w>\lfloor\alpha N\rfloor}\binom Nw\eta^w
\ \le\ 2^N\eta^{\lfloor\alpha N\rfloor+1}.
```

Choose $`0<\eta<1`$ so that $`2\eta^\alpha<1`$. This construction has positive rate per physical slot, even after the fixed factor $`nL`$ in the denominator. It allows arbitrary slot-dependent drift sequences within the stated tolerance. The tolerance is sufficient and can be small, since it uses a worst-case code-distance bound. The tensor-product assumption is essential to the expansion. At $`x+y\le1`$, the drift uncertainty class still includes the common-filter sequences used in the zero-capacity converse.

## Sources

- Barnum, Knill and Nielsen established the equivalence of entanglement transmission and strong subspace transmission criteria. [IEEE Trans. Inf. Theory 46, 1317–1329 (2000)](https://doi.org/10.1109/18.850671)
- Gottesman gives a stabilizer-code Gilbert–Varshamov bound in Chapter 2, Theorem 9 of his dissertation. [Stabilizer Codes and Quantum Error Correction](https://thesis.library.caltech.edu/2900/)

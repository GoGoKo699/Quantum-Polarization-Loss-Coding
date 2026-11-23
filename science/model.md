# A flagged link with drifting polarization axes

## One transmission

A carrier has two polarization states. A filter $`A:\mathbb C^2\to\mathbb C^2`$ is a contraction, and the receiver obtains either the surviving carrier or a distinguishable erasure flag $`|e\rangle`$. The channel and one complementary channel are

```math
\begin{aligned}
\Gamma_A(\rho)&=A\rho A^\dagger
  \oplus \mathrm{Tr}[(I-A^\dagger A)\rho]|e\rangle\langle e|,\\
\Gamma_A^c(\rho)&=\Gamma_B(\rho),\qquad B=\sqrt{I-A^\dagger A}.
\end{aligned}
```

An isometry sends $`|\psi\rangle`$ to $`A|\psi\rangle_B|e\rangle_E+|e\rangle_B B|\psi\rangle_E`$. Orthogonal flags remove cross terms in either marginal. Every missing carrier has an original position. For a fixed survivor set $`S`$, the environment holds the carriers in its complement $`L`$. The joint flagged branch results from $`A^{\otimes |S|}\otimes B^{\otimes |L|}`$, in survivor and lost order. Its weight can depend on the encoded state.

Write $`A=V D U`$ with $`D=\mathrm{diag}(\sqrt{x},\sqrt{y})`$ and $`0\le x,y\le1`$. The fixed squared singular values are the two polarization transmissivities. The loss basis on the input and the polarization orientation of surviving output are unknown.

## One coherence block

The same filter acts on every carrier of a known block of $`n`$ labeled transmissions. A pair of orientations may change arbitrarily between blocks. Conditional on a fixed orientation sequence the individual channel uses are a tensor product. In particular, this model supplies no shared calibration, axis records, feedback, or preshared entanglement. The singular values are fixed design parameters available for outer-code design. Carriers within a block remain distinguishable by position or time bin.

The receiver obtains the full erasure mask as a native channel output. An optical implementation needs a way to identify survivor positions without measuring the encoded polarization. Encoding, quantum storage during decoding and ideal joint gates are part of the abstract resources. The rate counts transmitted carriers, including lost carriers and padding.

## Error criterion and order of limits

For each fixed block size, use a sequence of encoders and decoders with entanglement fidelity approaching one, uniformly over the allowed orientation sequences. Normalize the logical qubits by the number of physical carriers. This is the orientation-independent, unassisted capacity $`Q_{\mathrm{rob}}(n)`$. In the long-coherence result, the number of blocks first grows at fixed $`n`$, then $`n`$ grows. The argument gives fixed blocks and uniform orientation performance even if no probability law for the axis drift is supplied.

| Resource or question | Model |
|---|---|
| Unknown degrees of freedom | One input and one output orientation per block |
| Known parameters | Block boundaries, carrier labels, and squared singular values $`x,y`$ |
| Classical record at the receiver | Labeled survival mask and local receiver measurements |
| Counted rate | Logical qubits per transmitted carrier |
| Perturbations | [Independent in-block filter deviations](drift.md) are a separate robustness calculation |

The [Schur receiver](schur_receiver.md) removes the unknown axes under the common-filter promise. The [capacity analysis](capacity.md) works out the resulting finite and long-block rates.

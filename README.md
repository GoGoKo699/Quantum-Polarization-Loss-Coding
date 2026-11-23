# Quantum Polarization Loss Coding

**Can a quantum link carry a qubit when its loss axes change between transmissions?** Send labeled carriers in blocks. Inside each block the polarization filter is common, while its two axes can change arbitrarily between blocks. A spin-zero encoder and a fixed Schur receiver remove both unknown axes from the channel seen by the outer code.

| Question | Result |
|---|---|
| When is a positive rate possible? | Exactly when $`x+y\gt 1`$ for coherence blocks of at least four carriers, where $`x,y`$ are the squared singular values of the filter. |
| What can four carriers do? | The fixed spin-zero scheme attains $`0.078`$ qubits per carrier at $`(x,y)=(0.8,0.4)`$. |
| What happens in long coherence blocks? | The best orientation-independent rate converges to the coherent information of the maximally mixed physical input, with a logarithmic-over-block-size bound on the gap. |

The four-carrier scheme has a rate per physical carrier of

```math
R_4(x,y)=\frac{\max\{0,(x+y-1)(1+x+y-2xy)\}}{4}.
```

With two surviving carriers, the receiver and environment each obtain a classical spin tag. These branches make zero net contribution to the coherent information. Replacing them with ordinary erasures transfers the logical system to the environment in the comparison channel and can lose the positive rate.

## One block as memory for a chirality decision

The [Quantum Chirality Receiver](https://github.com/GoGoKo699/Quantum-Chirality-Receiver/blob/8ed6c5e44188e7cb0e55e2dfec63f1ebc34de7e8/science/flagged-polarization-memory.md) uses the four-carrier block to carry its first specimen forward. Its staged receiver beats immediate first-specimen readout whenever both polarization transmissivities are positive. At unequal transmissivities $`x=0.490`$ and $`y=0.509`$, retaining the spin tag raises the worst-case success probability from 58.5342% to 58.8511% for a unit-volume triad. Both receivers have the full labeled survival mask. The link has zero orientation-independent quantum capacity at this spectrum. See the [decoded tag and mask effects](science/schur_receiver.md#the-two-survivor-tag-and-mask) for the channel behind the comparison.

## Read the science

| To inspect | Read |
|---|---|
| Channel, coherence promise and counted resources | [Model](science/model.md) |
| Encoding, receiver and four-carrier example | [Schur receiver](science/schur_receiver.md) |
| First-gap memory, with the spin tag retained or discarded | [Chirality decision](science/schur_receiver.md#using-a-single-block-for-a-chirality-decision) |
| Finite singlet capacity, all-code threshold and long-block law | [Capacity](science/capacity.md) |
| Sensitivity to variation within a block | [Drift](science/drift.md) |
| Prior results and the scope of the comparison | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

## Learn the project

The educational anchor is Bartlett, Rudolph and Spekkens, *Reference frames, superselection rules, and quantum information* (2007). The [source bridge](learning/BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md) connects their rotationally invariant codes to the loss model. The [30 milestones](learning/MILESTONES.md) follow the channel and encoder through the exact finite and asymptotic results. The [reading guide](llms.txt) maps technical questions to the corresponding proofs.

## Reproduce the finite checks

Run `python3 verification/verify.py` from the repository root with NumPy installed. The [verification notes](verification/README.md) describe the scalar probability checks and direct matrix calculations.

## Scope

The singular values are fixed design parameters. The receiver obtains the labeled survival flags without disturbing the transmitted polarization state. Every use counts, including lost and unused carriers. The rate concerns unassisted entanglement transmission with ideal encoding and decoding operations. Outer coding complexity and detector performance are open implementation questions.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

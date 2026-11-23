# Related work

## Quantum communication without aligned axes

Bartlett, Rudolph and Spekkens encode information in the multiplicities of collective rotations. Their communication rate approaches a qubit per carrier in the lossless setting. Their later review develops rotation twirling, noiseless subsystems and the relation to communication without a shared Cartesian frame. These are the structural ingredients behind the spin-zero encoder and the fixed Schur receiver. [Original paper](https://doi.org/10.1103/PhysRevLett.91.027901) · [Review](https://doi.org/10.1103/RevModPhys.79.555)

Migdał and Banaszek show how a decoherence-free code on carriers undergoing a common rotation preserves a qubit after one particle is removed. Their four-carrier example explains why every three-survivor branch can pass a qubit. The spin-dependent probabilities and two-survivor tags matter in the present capacity calculation because the filter attenuates the polarizations differently. [Particle-loss paper](https://doi.org/10.1103/PhysRevA.84.052318)

Bacon, Chuang and Harrow give efficient quantum circuits for Schur and Clebsch–Gordan transforms. These supply a route for compiling the inner encoder and decoder in an ideal gate model. The outer coding rate here follows from a capacity theorem, which does not itself give an efficient end-to-end implementation. [Schur transform circuits](https://doi.org/10.1103/PhysRevLett.97.170502)

## Polarization-dependent attenuation

Filippov introduces the flagged generalized erasure channel used here. The paper gives degradability and antidegradability criteria for specified filters, along with coherent-information superadditivity examples. In the present problem, one encoder and decoder must work uniformly over unknown input and output axes. The common-filter promise permits a spin-zero reduction whose degradability is controlled by the sum of the transmissivities, including cases where the specified-filter physical channel is not degradable. [Generalized erasure](https://doi.org/10.1088/1751-8121/abfd61)

Jones, Kirby and Brodsky measure and model polarization-dependent loss in fibers, including the consequences of relative loss orientations for the entanglement of photon pairs. That physical setting motivates the orientation assumption. The present calculation uses ideal flagged routing of the lost and surviving branches and does not infer experimental performance from the link model. [Entangled pairs under polarization-dependent loss](https://doi.org/10.1038/s41534-018-0107-x)

## Spin tags in sequential decisions

The [Quantum Chirality Receiver](https://github.com/GoGoKo699/Quantum-Chirality-Receiver/blob/8ed6c5e44188e7cb0e55e2dfec63f1ebc34de7e8/science/flagged-polarization-memory.md) studies a single use of the four-carrier decoded channel in a three-arrival handedness test. It optimizes the first instrument and the readout, and compares keeping the spin tag with keeping the labeled loss mask alone. The [Schur receiver](../science/schur_receiver.md#the-two-survivor-tag-and-mask) supplies the logical effects for that comparison. The rate analysis here and the sister decision theorem use the same decoded channel.

## Coding theorems and the adversarial model

The quantum coding theorem supplies achievable rates from coherent information. For degradable channels, the Devetak–Shor argument makes this optimization single-letter. Both tools apply to the reduced channel after the Schur receiver, which is identical for every allowed block orientation. [Quantum coding](https://arxiv.org/abs/quant-ph/0304127) · [Degradable channels](https://arxiv.org/abs/quant-ph/0311131)

Ahlswede, Bjelaković, Boche and Nötzel analyze coding against arbitrarily varying channel sequences. Their general converse framework explains the use of a mixture of admissible sequences to bound a code with uniform reliability. Here the two-orientation antidegradability witness and the Schur channel arise from the particular polarization filter. Neither requires shared randomness between the sender and receiver. [Arbitrarily varying quantum channels](https://arxiv.org/abs/1010.0418)

The [drift argument](../science/drift.md) uses positive-rate stabilizer families of linear distance, an established consequence of the quantum Gilbert–Varshamov bound. The capacity claim uses ideal coding operations. [Stabilizer code reference](https://arxiv.org/abs/quant-ph/9705052)

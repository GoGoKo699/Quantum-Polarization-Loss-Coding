# From a missing reference frame to polarization-dependent loss

A polarized carrier can arrive with its original state rotated and attenuated, or it can disappear. The sender and receiver know which physical slots were transmitted. The receiver learns the missing slots from the link. The polarization axes may change between blocks, so the task is to send quantum information without learning those axes.

The educational anchor is Stephen D. Bartlett, Terry Rudolph, and Robert W. Spekkens, *Reference frames, superselection rules, and quantum information*, **Reviews of Modern Physics 79**, 555–609 (2007). The section and equation identifiers below follow the authors' [arXiv v3 PDF](https://arxiv.org/pdf/quant-ph/0610030v3). The publication record gives the [journal version](https://doi.org/10.1103/RevModPhys.79.555).

## Targeted reading

| Anchor section | What to bring to the project | Milestones |
|---|---|---|
| §II.C, especially Eqs. (2.22)–(2.25) | Decompose a group representation into irreps and multiplicities. On each sector, twirling mixes the irrep and preserves the multiplicity. | [M07](MILESTONES.md#m07-gauge-and-multiplicity)–[M10](MILESTONES.md#m10-splitting-a-singlet-across-a-cut) |
| §III.A.2(a–c) | Count singlet and triplet sectors for two carriers and see how the spin-one-half sector of three carriers stores a logical qubit. | [M06](MILESTONES.md#m06-two-spins-and-total-spin)–[M08](MILESTONES.md#m08-counting-multiplicities), [M18](MILESTONES.md#m18-four-carrier-branch-structure) |
| §III.A.2(d), Eqs. (3.20)–(3.22) | Generalize the multiplicity count to many carriers and interpret an asymptotic cost of enforcing symmetry. | [M08](MILESTONES.md#m08-counting-multiplicities), [M13](MILESTONES.md#m13-the-four-carrier-encoder), [M25](MILESTONES.md#m25-the-cost-of-imposing-spin-zero) |
| §III.B, Eqs. (3.24)–(3.25) | See the construction of four-photon spin-zero states from singlet pairings and the appearance of a three-photon multiplicity when one photon is discarded. | [M13](MILESTONES.md#m13-the-four-carrier-encoder)–[M18](MILESTONES.md#m18-four-carrier-branch-structure) |

The review uses a noiseless channel in §III.A.2 to isolate the reference-frame problem. Its four-photon states in §III.B illustrate quantum key distribution. Here the task is unassisted quantum communication through a trace-preserving flagged loss channel. The same group decomposition is useful, and the [model](../science/model.md) gives the additional physical assumptions and definitions.

## Translate the spaces

| Review notation | Project notation | Meaning |
|---|---|---|
| $`\mathcal M_j`$ | $`V_{r,j}`$ | Spin-$`j`$ irrep in $`r`$ carriers. Collective rotations and collective filters act on this gauge space. |
| $`\mathcal N_j`$ | $`M_{r,j}`$ | Multiplicity space. Its coordinates distinguish copies of the same irrep and carry the encoded information. |
| $`c_j^{(N)}`$ | $`m(r,2j)=\dim M_{r,j}`$ | Number of copies of the spin sector. |
| $`R(\Omega)^{\otimes N}`$ | $`U^{\otimes r}`$ for a common input rotation | The same change of axes on every carrier, up to a physically irrelevant common phase. |
| $`\mathcal E_N`$ in Eq. (3.22) | The collective input twirl | A channel used in the large-block converse. The receiver also uses a Schur transform to identify and discard its gauge. |

For example, $`V_{3,1/2}`$ and $`M_{3,1/2}`$ both have dimension two. One factor describes the orientation of a surviving spin one half. The other describes how three carriers can add up to that spin. The latter carries the logical qubit after one loss from a four-carrier singlet.

## Carry the mechanism into this project

In the review the collective rotation acts on the gauge alone. In the [Schur receiver](../science/schur_receiver.md), the survival map with amplitude $`A`$ and complementary loss amplitude $`B=\sqrt{I-A^\dagger A}`$ act on the two sides of a cut. Their actions are generally nonunitary. For a fixed set of surviving slots $`S`$ and a fixed spin $`j`$, they act on the two gauge factors only. Those factors began in a shared spin-$`j`$ singlet. The common input rotation cancels on that singlet, and the output rotations act on factors that are discarded. The resulting multiplicity channel still carries the outcome $`(S,j)`$, with a weight determined by the two transmission probabilities.

Four carriers give a direct illustration. With three or four survivors, the receiver's multiplicity has room for the qubit. With at most one survivor, the environment's multiplicity has room for it. With two survivors, the two sides can both retain the spin label, while each fixed spin multiplicity is one dimensional.

At $`x=0.8`$ and $`y=0.4`$, the quantum branches give receiver weight $`0.4608`$ and environment weight $`0.1488`$. The other branches contribute equal classical entropy to both sides. For the uniform logical input, the resulting coherent information per transmitted carrier is

```math
\frac{0.4608-0.1488}{4}=0.078.
```

Sending one logical qubit through a single block remains a probabilistic process. The rate describes outer coding across many blocks of the same reduced channel. An ordinary erasure decoder that discards all two-loss outcomes would retain quantum information in fewer than half the blocks. The [capacity proof](../science/capacity.md) explains how the sector labels enter the retained output and why the difference of the two weights is the relevant rate for the singlet architecture.

## Read the capacity proof in order

1. The finite singlet channel keeps every ordered loss flag and spin label. Use the Schur multiplicities to compute the receiver and environment entropy difference.
2. A polarization exchange and a physical postfilter implement degradation or antidegradation on invariant inputs. The resulting concavity and permutation symmetry select the uniform singlet for the finite singlet rate.
3. A fair coin over two allowed orientations gives an all-encoder antidegradability converse at or below mean transmission one half. The four-carrier rate supplies the achievability above it.
4. Let the number of blocks grow for each fixed block length, then take long coherent blocks. Compare the uniform singlet's entropy with that of a product maximally mixed input. Use an orientation average and its environment dimension to bound unrestricted encoders.

The proof uses coherent information, degradation, and channel entropy inequalities in addition to the anchor's representation theory. The [scientific attribution](../references/RELATED_WORK.md) identifies their sources. The [within-block drift analysis](../science/drift.md) identifies where the exact cancellation depends on a common filter. Work through the [milestones](MILESTONES.md) and use the [verification calculations](../verification/README.md) to check the four-carrier numbers.

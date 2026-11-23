# Project understanding map

The first 12 milestones build the model from one physical carrier to entanglement transmission across many blocks. The remaining 18 build the receiver, derive the finite and limiting rates, and connect the guarantees to the channel assumptions.

Read the [educational bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md) alongside this map. Each milestone points to the scientific account that supplies the model or proof.

| Milestones | Connection |
|---|---|
| [M01](#m01-a-polarization-qubit)–[M05](#m05-blocks-and-adversarial-axes) | One lossy carrier and the many-block task |
| [M06](#m06-two-spins-and-total-spin)–[M12](#m12-the-complete-coding-problem) | Total spin, multiplicity, and coding rates |
| [M13](#m13-the-four-carrier-encoder)–[M19](#m19-four-carrier-rate-and-worked-case) | The fixed decoder and its four-carrier rate |
| [M20](#m20-degradation-via-a-physical-postfilter)–[M26](#m26-the-large-block-all-code-bound) | Degradation, the all-code threshold, and the limiting rate |
| [M27](#m27-within-block-variation)–[M30](#m30-the-complete-communication-story) | Robustness, attribution, reproduction, and synthesis |

## Phase I. Background and preliminaries

### M01 A polarization qubit

**Central question.** What travels in one use of the link?

**Understanding target.** Describe one labeled carrier as a qubit with two orthogonal polarization directions. Name the additional vacuum symbol that the receiver can distinguish from either direction.

**Prerequisites.** None within this map.

**Conceptual connection.** The label identifies a physical slot, so a missing carrier can become a location flag while the polarization of every arriving carrier remains quantum.

**Sources.** [Channel model and assumptions](../science/model.md).

### M02 The two transmission axes

**Central question.** What does it mean for the fiber to lose one polarization more often?

**Understanding target.** Use the singular-value decomposition of the survival amplitude to distinguish the input axes, the output axes, and the two transmission probabilities.

**Prerequisites.** [M01](#m01-a-polarization-qubit).

**Conceptual connection.** The loss parameters can be stable even while the directions that define them change.

**Sources.** [Channel model and assumptions](../science/model.md).

### M03 Flagged loss as a quantum channel

**Central question.** How can a polarization-dependent disappearance remain a linear channel?

**Understanding target.** Write the surviving block as the filtered, subnormalized polarization state and the missing block as its complementary probability times a vacuum flag.

**Prerequisites.** [M01](#m01-a-polarization-qubit), [M02](#m02-the-two-transmission-axes).

**Conceptual connection.** The output contains both the polarization distortion of a survivor and the probability of its arrival. Both enter coding rates.

**Sources.** [Channel model and assumptions](../science/model.md).

### M04 The complementary receiver

**Central question.** Where does the quantum state go when a carrier disappears?

**Understanding target.** Construct the one-carrier isometry by giving the filtered polarization to one side and a vacuum to the other in each orthogonal branch. Identify which side receives the loss filter.

**Prerequisites.** [M03](#m03-flagged-loss-as-a-quantum-channel).

**Conceptual connection.** The same flag pattern organizes both marginal outputs. Entropies from these two views determine coherent information.

**Sources.** [Channel model and assumptions](../science/model.md).

### M05 Blocks and adversarial axes

**Central question.** Which part of the channel stays the same over several uses?

**Understanding target.** State the model with labeled carrier slots, a common survival matrix within a known block, fixed transmission probabilities, and arbitrary axis choices between blocks. Describe the unassisted communication task including preservation of reference entanglement.

**Prerequisites.** [M02](#m02-the-two-transmission-axes), [M03](#m03-flagged-loss-as-a-quantum-channel), [M04](#m04-the-complementary-receiver).

**Conceptual connection.** Uniform success over axis sequences permits an averaged channel to upper-bound performance, while an exact common reduction permits a single working code.

**Sources.** [Channel model and assumptions](../science/model.md).

### M06 Two spins and total spin

**Central question.** What can a pair of spins say about a common rotation?

**Understanding target.** Decompose two spin-half carriers into a spin-zero singlet and a spin-one triplet, and explain the different actions of a common rotation on the two sectors.

**Prerequisites.** [M01](#m01-a-polarization-qubit).

**Conceptual connection.** The singlet fixes a relational property without requiring either party to name the same polarization direction.

**Sources.** [Channel model and assumptions](../science/model.md). [Educational bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md), §III.A.2(b).

### M07 Gauge and multiplicity

**Central question.** How can several copies of the same spin sector hold a qubit?

**Understanding target.** In a fixed total-spin sector, identify the irrep coordinates as the spin gauge and the multiplicity coordinates as the label of equivalent copies. Explain which coordinates collective rotations can change.

**Prerequisites.** [M06](#m06-two-spins-and-total-spin).

**Conceptual connection.** It is possible to lose all information about absolute orientation and still preserve information in the multiplicity.

**Sources.** [Spin decomposition and receiver](../science/schur_receiver.md). [Educational bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md), §II.C and III.A.2(c).

### M08 Counting multiplicities

**Central question.** Why is the four-carrier spin-zero space two dimensional?

**Understanding target.** Compute a multiplicity as the difference of adjacent binomial weight counts. Recover the multiplicity-two sectors for three surviving spin-half carriers at spin one half and for four carriers at spin zero.

**Prerequisites.** [M06](#m06-two-spins-and-total-spin), [M07](#m07-gauge-and-multiplicity).

**Conceptual connection.** These two multiplicities account for the quantum output recovered after zero or one loss.

**Sources.** [Spin decomposition and receiver](../science/schur_receiver.md). [Educational bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md), §III.A.2(d).

### M09 Twirling about an unknown reference

**Central question.** What does averaging over all axis rotations remove?

**Understanding target.** Distinguish removal of cross-sector coherence, replacement of the gauge by its maximally mixed state, and preservation of the multiplicity information.

**Prerequisites.** [M05](#m05-blocks-and-adversarial-axes), [M07](#m07-gauge-and-multiplicity).

**Conceptual connection.** An axis average contributes to a worst-case converse. The singlet receiver instead works for every axis choice in the stated model.

**Sources.** [Spin decomposition and receiver](../science/schur_receiver.md). [Educational bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md), §II.C and III.A.2.

### M10 Splitting a singlet across a cut

**Central question.** What can the surviving and missing sides share when the whole block has spin zero?

**Understanding target.** Explain why the two sides must have the same spin, with a singlet across their gauge registers and arbitrary multiplicity coordinates on the two sides.

**Prerequisites.** [M04](#m04-the-complementary-receiver), [M06](#m06-two-spins-and-total-spin), [M07](#m07-gauge-and-multiplicity).

**Conceptual connection.** The loss flag specifies the cut. A Schur transform then exposes the spin sector and the surviving multiplicity.

**Sources.** [Spin decomposition and receiver](../science/schur_receiver.md). [Educational bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md), §III.A.2(b) and III.A.2(d).

### M11 Coherent information with flags

**Central question.** How do quantum and classical branches contribute to a communication rate?

**Understanding target.** Form the difference of receiver and environment output entropies. Explain why common classical flag entropy cancels and how degradability makes the one-block coherent-information maximum sufficient.

**Prerequisites.** [M04](#m04-the-complementary-receiver), [M05](#m05-blocks-and-adversarial-axes).

**Conceptual connection.** A branch giving identical classical information to the two sides can contribute zero to the entropy difference while remaining part of the complete channel.

**Sources.** [Capacity proofs and examples](../science/capacity.md).

### M12 The complete coding problem

**Central question.** Which guarantees describe the block interface, and which describe many-block communication?

**Understanding target.** Distinguish exact removal of axis dependence in an inner block from vanishing error under outer coding. Charge every transmitted carrier and keep the number of coding blocks distinct from the length of an axis-coherent block.

**Prerequisites.** [M05](#m05-blocks-and-adversarial-axes), [M07](#m07-gauge-and-multiplicity), [M10](#m10-splitting-a-singlet-across-a-cut), [M11](#m11-coherent-information-with-flags).

**Conceptual connection.** The rest of the route builds one fixed logical channel, then uses it to characterize the available rates.

**Sources.** [Channel model and assumptions](../science/model.md).

## Phase II. Narrative and innovation

### M13 The four-carrier encoder

**Central question.** Where is the logical qubit put before any losses occur?

**Understanding target.** Describe an isometry into the two-dimensional spin-zero space and explain how two independent singlet pairings can provide a basis after orthogonalization.

**Prerequisites.** [M08](#m08-counting-multiplicities), [M10](#m10-splitting-a-singlet-across-a-cut), [M12](#m12-the-complete-coding-problem).

**Conceptual connection.** Four carriers create a gauge-invariant input and a two-dimensional logical degree of freedom before the loss pattern is known.

**Sources.** [Spin decomposition and receiver](../science/schur_receiver.md). [Educational bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md), §III.A.2(d) and III.B.

### M14 The survival filter in spin coordinates

**Central question.** Why does polarization-selective attenuation respect the multiplicity space?

**Understanding target.** Follow a common nonunitary filter on a Schur sector through its singular-value factors. Explain that collective factors act on the representation coordinates and leave equivalent copies unchanged.

**Prerequisites.** [M02](#m02-the-two-transmission-axes), [M07](#m07-gauge-and-multiplicity), [M10](#m10-splitting-a-singlet-across-a-cut).

**Conceptual connection.** This extends the lossless rotation mechanism to amplitude filtering while allowing the survival probability to depend on the input.

**Sources.** [Spin decomposition and receiver](../science/schur_receiver.md).

### M15 The receiver for a chosen loss pattern

**Central question.** How does Bob retrieve information without naming a polarization axis?

**Understanding target.** Given the labels of surviving carriers, describe applying their Schur transform, retaining the total-spin label and multiplicity, and discarding the spin gauge.

**Prerequisites.** [M05](#m05-blocks-and-adversarial-axes), [M10](#m10-splitting-a-singlet-across-a-cut), [M13](#m13-the-four-carrier-encoder), [M14](#m14-the-survival-filter-in-spin-coordinates).

**Conceptual connection.** The operations depend on the positions that survived, which the channel supplies, and are fixed for every choice of unknown input and output axes.

**Sources.** [Spin decomposition and receiver](../science/schur_receiver.md).

### M16 Exact orientation cancellation

**Central question.** Why is the whole reduced channel identical across blocks with different axes?

**Understanding target.** Trace a split singlet through the paired survival and loss filters. Explain why the shared input rotation cancels, the output rotation stays on discarded gauges, and the remaining branch weights depend only on the spectrum.

**Prerequisites.** [M04](#m04-the-complementary-receiver), [M10](#m10-splitting-a-singlet-across-a-cut), [M14](#m14-the-survival-filter-in-spin-coordinates), [M15](#m15-the-receiver-for-a-chosen-loss-pattern).

**Conceptual connection.** This identity holds with a reference entangled with the logical input, making the same effective channel usable in a many-block code.

**Sources.** [Spin decomposition and receiver](../science/schur_receiver.md).

### M17 Reading the finite-block formula

**Central question.** How do the loss flags, spin weights, and multiplicities combine numerically?

**Understanding target.** Identify the combinatorial multiplicities, the filtered gauge norm and the number of spatial flags in the joint probability for a survivor count and spin label.

**Prerequisites.** [M08](#m08-counting-multiplicities), [M10](#m10-splitting-a-singlet-across-a-cut), [M11](#m11-coherent-information-with-flags), [M16](#m16-exact-orientation-cancellation).

**Conceptual connection.** The probability formula and the log ratio of multiplicities give an inspectable computation for the uniform-singlet coherent information.

**Sources.** [Capacity proofs and examples](../science/capacity.md).

### M18 Four-carrier branch structure

**Central question.** What reaches each side after zero, one, two, three, or four losses?

**Understanding target.** Identify the branches that pass a logical qubit to the receiver or environment. For a two-survivor mask, derive both spin-tag effects and add them to get the effect of the mask alone. Check how unequal transmissivities change that effect.

**Prerequisites.** [M11](#m11-coherent-information-with-flags), [M13](#m13-the-four-carrier-encoder), [M15](#m15-the-receiver-for-a-chosen-loss-pattern), [M17](#m17-reading-the-finite-block-formula).

**Conceptual connection.** A tag reveals which spin sector occurred. A labeled mask can still carry partial information about that sector when the two polarizations have different transmission probabilities.

**Sources.** [Two-survivor tag and mask](../science/schur_receiver.md#the-two-survivor-tag-and-mask). [Educational bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md), §III.B, Eq. (3.24).

### M19 Four-carrier rate and worked case

**Central question.** How can a receiver with fewer than half all blocks carrying a qubit still communicate?

**Understanding target.** At transmission probabilities 0.8 and 0.4, reproduce the receiver and environment quantum branch weights 0.4608 and 0.1488. Explain why their difference gives 0.078 qubits per physical carrier for this code.

**Prerequisites.** [M17](#m17-reading-the-finite-block-formula), [M18](#m18-four-carrier-branch-structure).

**Conceptual connection.** The sector-resolved receiver uses classical tags on the remaining branches. The comparison to an ordinary erasure channel keeps the same physical block and changes only what is retained.

**Sources.** [Capacity proofs and examples](../science/capacity.md).

### M20 Degradation via a physical postfilter

**Central question.** How can one receiver simulate the other when transmission is large enough?

**Understanding target.** Describe the exchanged-axis loss filter and interpret the contraction test when the two transmission probabilities sum to at least one. Reverse the argument for antidegradation in the singlet construction.

**Prerequisites.** [M04](#m04-the-complementary-receiver), [M10](#m10-splitting-a-singlet-across-a-cut), [M11](#m11-coherent-information-with-flags), [M16](#m16-exact-orientation-cancellation).

**Conceptual connection.** A polarization exchange is harmless to a rotationally invariant encoded state, which makes a physical filtering relation into a simulation of the logical outputs.

**Sources.** [Capacity proofs and examples](../science/capacity.md).

### M21 Optimal input in the singlet architecture

**Central question.** Why does the uniform singlet suffice for computing capacity?

**Understanding target.** Use permutation covariance, irreducibility of the spin-zero multiplicity, and concavity of coherent information under degradability to justify averaging the input.

**Prerequisites.** [M07](#m07-gauge-and-multiplicity), [M11](#m11-coherent-information-with-flags), [M17](#m17-reading-the-finite-block-formula), [M20](#m20-degradation-via-a-physical-postfilter).

**Conceptual connection.** The capacity is evaluated by one explicit input for the specified architecture. Coding performance with arbitrary finite-block encodings is a separate question.

**Sources.** [Capacity proofs and examples](../science/capacity.md).

### M22 A two-orientation adversary

**Central question.** Which adversary can rule out all codes when average transmission is at most one half?

**Understanding target.** Choose with equal probability between two common input axes related by a polarization exchange. Track the adversary's coin in the environment and use the reverse contraction to simulate the averaged receiver channel.

**Prerequisites.** [M04](#m04-the-complementary-receiver), [M05](#m05-blocks-and-adversarial-axes), [M20](#m20-degradation-via-a-physical-postfilter).

**Conceptual connection.** This gives an antidegradable instance obtained by averaging permitted sequences. A uniform code must also work for that average, even if its own inputs are outside the singlet space.

**Sources.** [Capacity proofs and examples](../science/capacity.md).

### M23 The sharp positive-rate threshold

**Central question.** How do the attainable four-carrier rate and the worst-case converse meet?

**Understanding target.** Combine the finite singlet rate and the all-code converse to prove positivity exactly when the two transmission probabilities sum to more than one, for each coherence length of at least four.

**Prerequisites.** [M12](#m12-the-complete-coding-problem), [M19](#m19-four-carrier-rate-and-worked-case), [M21](#m21-optimal-input-in-the-singlet-architecture), [M22](#m22-a-two-orientation-adversary).

**Conceptual connection.** For larger blocks a four-carrier construction can be used with the remaining carriers ignored. Counting those carriers changes the rate while preserving positivity at fixed length.

**Sources.** [Capacity proofs and examples](../science/capacity.md).

### M24 The polarization-resolved limiting rate

**Central question.** What single-carrier entropy balance describes long coherent blocks?

**Understanding target.** Evaluate the difference of the polarization entropies of receiver and environment outputs at maximally mixed input, with the survival and loss probabilities as weights.

**Prerequisites.** [M04](#m04-the-complementary-receiver), [M11](#m11-coherent-information-with-flags), [M23](#m23-the-sharp-positive-rate-threshold).

**Conceptual connection.** The resulting rate depends on the full transmission spectrum even though its positivity boundary depends on the sum.

**Sources.** [Capacity proofs and examples](../science/capacity.md).

### M25 The cost of imposing spin zero

**Central question.** How much rate can enforcing the encoder's symmetry remove?

**Understanding target.** Relate the entropy deficit of the uniform singlet to the Catalan dimension. Apply relative-entropy contraction to bound the change from product-input output entropies.

**Prerequisites.** [M08](#m08-counting-multiplicities), [M11](#m11-coherent-information-with-flags), [M21](#m21-optimal-input-in-the-singlet-architecture), [M24](#m24-the-polarization-resolved-limiting-rate).

**Conceptual connection.** The encoding space loses only logarithmically many qubits compared to unrestricted carrier space. This becomes a vanishing rate cost as block length grows.

**Sources.** [Capacity proofs and examples](../science/capacity.md).

### M26 The large-block all-code bound

**Central question.** What prevents an unrestricted encoder from beating the limiting rate?

**Understanding target.** Average one allowed common input orientation across the entire code, bound the entropy cost of the Schur twirl's environment, and use the physical postfilter on invariant inputs to order the receiver and environment entropy deficits.

**Prerequisites.** [M09](#m09-twirling-about-an-unknown-reference), [M20](#m20-degradation-via-a-physical-postfilter), [M22](#m22-a-two-orientation-adversary), [M24](#m24-the-polarization-resolved-limiting-rate), [M25](#m25-the-cost-of-imposing-spin-zero).

**Conceptual connection.** Together with the spin-zero lower bound, the upper argument identifies the limiting rate and keeps both orders of limits explicit.

**Sources.** [Capacity proofs and examples](../science/capacity.md).

### M27 Within-block variation

**Central question.** Which part of the construction is sensitive to axes that vary within one block?

**Understanding target.** Identify where a common input rotation was used in the exact reduction. Relate a bound on within-block channel changes to the perturbed inner output and distinguish a finite robustness bound from exact cancellation.

**Prerequisites.** [M05](#m05-blocks-and-adversarial-axes), [M16](#m16-exact-orientation-cancellation), [M19](#m19-four-carrier-rate-and-worked-case), [M23](#m23-the-sharp-positive-rate-threshold).

**Conceptual connection.** This links the reported stability guarantee to a physical specification of coherence time and to the nominal rate margin available to the outer code.

**Sources.** [Within-block drift](../science/drift.md).

### M28 The provenance of the coding ingredients

**Central question.** Which ideas come from reference-frame work, and which address polarization-dependent loss here?

**Understanding target.** Trace rotational multiplicities, single-particle-loss immunity, and the flagged loss model to their sources. Identify the role of the two-survivor tags, the orientation-free filter reduction, and the worst-case capacity bounds.

**Prerequisites.** [M09](#m09-twirling-about-an-unknown-reference), [M13](#m13-the-four-carrier-encoder), [M16](#m16-exact-orientation-cancellation), [M18](#m18-four-carrier-branch-structure), [M23](#m23-the-sharp-positive-rate-threshold), [M26](#m26-the-large-block-all-code-bound).

**Conceptual connection.** The literature comparison connects inherited mechanisms to the precise claims of the present channel model.

**Sources.** [Related work](../references/RELATED_WORK.md). [Educational bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md), §II.C, III.A.2 and III.B.

### M29 Checking proof against computation

**Central question.** What can finite calculations verify in the four-carrier example?

**Understanding target.** Compare the spin-sector sum with direct matrix evaluation at several orientations and check normalization and the scalar-transmission case. For four carriers, test the two-survivor tag and mask effects on every logical matrix unit.

**Prerequisites.** [M17](#m17-reading-the-finite-block-formula), [M19](#m19-four-carrier-rate-and-worked-case), [M22](#m22-a-two-orientation-adversary), [M26](#m26-the-large-block-all-code-bound), [M27](#m27-within-block-variation).

**Conceptual connection.** Numerical reproduction catches normalization, indexing, and branch mistakes. The all-axis and all-code statements follow from the mathematical proofs.

**Sources.** [Finite verification](../verification/README.md).

### M30 The complete communication story

**Central question.** What does the sender gain and what remains a physical requirement?

**Understanding target.** Reconstruct the path from labeled carriers and the spin-zero encoder through the fixed Schur receiver to the sharp threshold and limiting rate. Describe the fixed spectrum, flagged locations, common-axis assumption, unassisted resources, and within-block variation addressed in the robustness result.

**Prerequisites.** [M12](#m12-the-complete-coding-problem), [M19](#m19-four-carrier-rate-and-worked-case), [M23](#m23-the-sharp-positive-rate-threshold), [M26](#m26-the-large-block-all-code-bound), [M27](#m27-within-block-variation), [M28](#m28-the-provenance-of-the-coding-ingredients), [M29](#m29-checking-proof-against-computation).

**Conceptual connection.** Compare the two thresholds in the example with transmissivities 0.490 and 0.509. Determine why one fixed block still helps decide handedness, and identify what extra information is available when the spin tag is retained.

**Sources.** [Capacity proofs and examples](../science/capacity.md). [Chirality decision](../science/schur_receiver.md#using-a-single-block-for-a-chirality-decision).

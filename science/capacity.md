# Quantum capacity under polarization-dependent loss

## Channel and communication task

A physical carrier is a polarization qubit in a labeled time slot. Its survival operator is a contraction $`A`$. The receiver either obtains a surviving qubit or an orthogonal erasure flag in that slot. Let $`B=\sqrt{I-A^\dagger A}`$. A channel and a complementary channel are

```math
\begin{aligned}
\Gamma_A(\rho) &= A\rho A^\dagger \oplus
     \mathrm{Tr}(B\rho B^\dagger)\lvert e\rangle\!\langle e\rvert,\\
\Gamma_A^c(\rho) &= B\rho B^\dagger \oplus
     \mathrm{Tr}(A\rho A^\dagger)\lvert e\rangle\!\langle e\rvert .
\end{aligned}
```

They follow from the isometry $`\lvert\psi\rangle\mapsto A\lvert\psi\rangle_B\lvert e\rangle_E+\lvert e\rangle_B B\lvert\psi\rangle_E`$, with output subscripts denoting Bob and the environment. The erasure probability can depend on the input polarization.

A known block comprises $`n`$ physical slots. In each block $`A=VDU`$, where $`D=\mathrm{diag}(\sqrt{x},\sqrt{y})`$ and $`0\le x,y\le1`$. The spectrum $`(x,y)`$ is fixed and available for code design. The two unitaries are unknown and can change arbitrarily from block to block. For any fixed sequence of operators, the physical channel is a tensor product. Receiver survival flags preserve the indicated quantum outputs. These flags, coherent encoding and joint quantum decoding are part of the model.

Write $`Q_n(x,y)`$ for the orientation-independent capacity $`Q_{\mathrm{rob}}(n)`$ of the [model](model.md), displaying the fixed spectrum explicitly. For fixed $`n`$, a deterministic code must have entanglement fidelity tending to one uniformly over all axis sequences as the number of blocks grows. Each transmitted slot counts, including lost or ignored slots. The encoder and decoder use no feedback, preshared entanglement, shared randomness, or pilot calibration of the axes.

## Spin-zero encoding and the receiver

For even $`n`$, use the spin-zero space $`\mathcal H_{n,0}`$ of $`n`$ qubits. Write $`\mathcal M_{r,j}`$ for the multiplicity space of spin $`j`$ among $`r`$ qubits and $`\mathcal V_j`$ for its $`2j+1`$ dimensional spin space. If the survival flag is the set $`S`$, put $`s=|S|`$ and $`\ell=n-s`$. Decomposing each side of this cut into spins identifies the global spin-zero space with

```math
\bigoplus_j
    \mathcal M_{s,j}\otimes\mathcal M_{\ell,j}
    \otimes\mathrm{span}\{\lvert\Omega_j\rangle\},
\qquad
\lvert\Omega_j\rangle
  =\frac{1}{\sqrt{2j+1}}\sum_{a=-j}^j
      (-1)^{j-a}\lvert j,a\rangle\lvert j,-a\rangle .
```

The sum uses the spins appearing on both sides. Each common input rotation acts by a scalar on spin zero, and a tensor power of any one-qubit matrix acts on the spin space only within each sector. In the survival branch $`S`$, the surviving carriers see $`(VD)^{\otimes s}`$ and the lost carriers see $`L^{\otimes\ell}`$ after removing the common input rotation, where $`L=\mathrm{diag}(\sqrt{1-x},\sqrt{1-y})`$.

The receiver applies a Schur transform to the surviving qubits, reads their spin $`j`$, and discards the spin register. It retains $`(S,j)`$ and the surviving multiplicity. For fixed $`S,j`$, write $`\Pi_{S,j}`$ for the projection in the cut decomposition. The reduced receiver channel $`\Phi_n`$ is

```math
\Phi_n(\rho)=\bigoplus_{S,j} w_{s,\ell,j}\,
 \mathrm{Tr}_{\mathcal M_{\ell,j}}(\Pi_{S,j}\rho\Pi_{S,j}).
```

Here $`w_{s,\ell,j}`$ is the squared norm of the filtered spin singlet on the two spin registers. The left rotation $`V`$ only rotates a discarded register, so this channel is identical for every allowed choice of axes. An outer code across blocks therefore sees the same ordinary memoryless channel $`\Phi_n`$ for every sequence, including sequences in which the orientations change at every block boundary.

The corresponding environment channel carries the same classical labels $`(S,j)`$ and the lost multiplicity. In both physical marginals, a conditional spin density matrix tensors with the corresponding logical multiplicity state. The two spin density matrices have the same entropy, since they are marginals of the same pure filtered spin state. Thus dropping the spin registers leaves coherent information unchanged. This follows by subtracting the two block-diagonal entropies, including their identical label distributions.

## Exact rate with spin-zero input

Start with the canonical diagonal filter. If $`x+y\ge1`$, the receiver-side polarization contraction

```math
F_+=\mathrm{diag}\!\left(\sqrt{\frac{1-y}{x}},
                              \sqrt{\frac{1-x}{y}}\right)
```

turns $`D`$ into $`XLX`$, where $`X`$ interchanges the two polarizations. An entry with denominator zero is arbitrary if its numerator also vanishes. Applying $`\Gamma_{F_+}`$ to each surviving carrier, and preserving existing erasure flags, realizes $`\Gamma_{XLX}^{\otimes n}`$ from $`\Gamma_D^{\otimes n}`$. Collective input $`X^{\otimes n}`$ acts by a phase on spin-zero vectors. Applying an output $`X`$ to each surviving slot therefore gives the canonical environment channel $`\Gamma_L^{\otimes n}`$ on this input space. Each physical canonical marginal can be reconstructed from its reduced marginal by reattaching the known spin density matrix conditioned on $`(S,j)`$. Reattachment, the polarization filter, and removal of the environment spin register together give a degrading channel for $`\Phi_n`$. For $`x+y\le1`$, reverse the argument with a filter sending $`L`$ to $`XDX`$. This gives an antidegrading channel. The reattachment and polarization filters prove these channel relations. The physical receiver uses the Schur transform and outer decoding.

In the degradable regime the capacity is single-letter and coherent information is concave in its input. Physical permutations act covariantly on the flags and on the multiplicity registers of both outputs. Their representation on $`\mathcal H_{n,0}`$ is the irreducible symmetric-group representation with Young diagram $`(n/2,n/2)`$. Consequently, averaging any code-space input over these permutations gives the uniform spin-zero state $`\tau_n`$ and cannot reduce its coherent information. In the antidegradable regime the capacity is zero.

For an explicit formula, put $`t=2j`$ and define

```math
m_{r,t}=\binom{r}{(r-t)/2}-\binom{r}{(r-t)/2-1},
\qquad
d_n=m_{n,0}=\frac{1}{n/2+1}\binom{n}{n/2}.
```

An unavailable or out-of-range sector has zero multiplicity. In each available sector,

```math
w_{s,\ell,t/2}=
 (xy)^{(s-t)/2}\big((1-x)(1-y)\big)^{(\ell-t)/2}
 \frac{1}{t+1}
 \sum_{a=0}^{t}\big(x(1-y)\big)^{t-a}
                    \big(y(1-x)\big)^a .
```

This follows by representing the spin part of a diagonal matrix on $`r`$ qubits as its degree-$`t`$ symmetric power times its determinant to power $`(r-t)/2`$. Each allowed $`a`$ corresponds to paired complementary weights in $`\lvert\Omega_{t/2}\rangle`$. At endpoints a factor with exponent zero is one.

Both multiplicity states in each branch of the uniform input are maximally mixed. The exact spin-zero rate per physical slot is

```math
R_n^{(0)}(x,y)=\frac{1}{n}
 \max\left\{0,\
 \sum_{s=0}^{n}\ \sum_{\substack{t:\ m_{s,t}m_{n-s,t}>0}}
 \binom ns\frac{m_{s,t}m_{n-s,t}}{d_n}\,
 w_{s,n-s,t/2}\log_2\frac{m_{s,t}}{m_{n-s,t}}\right\}.
```

The factor $`\binom ns`$ counts equally weighted survival sets. The logarithm gives the difference of the two multiplicity entropies. The outer coding theorem applied to the reduced channel gives entanglement transmission at any rate below this formula.

### The four-carrier code

A convenient basis for the two-dimensional spin-zero space couples carriers $`1,2`$ and $`3,4`$ first. One codeword is a product of pair singlets. The other couples the two pair triplets to total spin zero,

```math
\lvert0_L\rangle=\lvert s\rangle\lvert s\rangle,\qquad
\lvert1_L\rangle=
 \frac{\lvert t_+\rangle\lvert t_-\rangle
       -\lvert t_0\rangle\lvert t_0\rangle
       +\lvert t_-\rangle\lvert t_+\rangle}{\sqrt3}.
```

With four or three survivors, Bob retains the full logical qubit. With zero or one survivor, the environment retains it. For two survivors, the two possible spins of a surviving pair both have multiplicity one. The two spin labels give a rank-one logical measurement recorded on both sides. These branches make zero contribution to coherent information for the uniform input. Replacing them by a single erasure discards that distinction.

The probabilities of the full logical qubit reaching each side are

```math
p_B=2xy(x+y)-3x^2y^2,\qquad
p_E=2(1-x)(1-y)(2-x-y)-3(1-x)^2(1-y)^2 .
```

The spin-zero capacity is $`\max(0,p_B-p_E)/4`$, or

```math
R_4^{(0)}(x,y)
=\frac14\max\{0,\ (x+y-1)(1+x+y-2xy)\}.
```

For $`(x,y)=(0.8,0.4)`$, $`p_B=0.4608`$ and $`p_E=0.1488`$. The achievable rate is $`0.078`$ qubits per physical slot. An ordinary-erasure reduction declaring every two-loss branch a failure has capacity zero, since $`p_B<1/2`$. Passive single-carrier balancing to the weaker transmission $`y=0.4`$ also produces a zero-capacity ordinary erasure channel.

## Capacity threshold over all codes

If $`x+y\le1`$, consider a legal channel sequence with one hidden fair coin $`b`$ per block and use $`A_b=DX^b`$ for that block. A Stinespring isometry for the averaged block is the coherent sum of the two block isometries with amplitudes $`1/\sqrt2`$, using orthogonal coin labels in the environment. Measuring that label produces the environment channel $`\Gamma_{LX^b}^{\otimes n}`$ for each outcome $`b`$. The environment filter $`F_-=DXL^{-1}`$ is a contraction precisely when $`x\le1-y`$ and $`y\le1-x`$. As above, any zero denominator is handled on the unused subspace. Acting on each available polarization, the filter gives

```math
F_-LX^b=DX^{b\oplus1}.
```

The distribution is unchanged when the hidden coin is flipped. This is an antidegrading map for the averaged block channel, which has zero quantum capacity. A code reliable for every orientation sequence would also be reliable on its average. This gives an unrestricted converse.

For $`x+y>1`$, use the four-carrier code in four designated slots of each block and ignore the unused slots. This achieves $`4R_4^{(0)}(x,y)/n>0`$ whenever $`n\ge4`$. Hence

```math
Q_n(x,y)>0 \quad\Longleftrightarrow\quad x+y>1
\qquad(n\ge4).
```

This threshold concerns all encoders and decoders. The formula for $`R_n^{(0)}`$ concerns the spin-zero architecture. Optimizing the unrestricted rate at each fixed $`n`$ above threshold is a separate problem.

## Capacity in the long-coherence limit

Let $`h_2`$ be binary entropy in bits and write

```math
C(x,y)= I_c(I/2,\Gamma_D)
=\frac{x+y}{2}h_2\!\left(\frac{x}{x+y}\right)
 -\frac{2-x-y}{2}h_2\!\left(\frac{1-x}{2-x-y}\right).
```

A term with zero prefactor is zero. This is the one-carrier coherent information of the maximally mixed state. For fixed $`d=|x-y|`$, the function $`s\mapsto (s/2)h_2((s+d)/(2s))`$ increases strictly for $`s>d`$ and is continuous at the endpoint. The two terms use $`s=x+y`$ and $`s=2-x-y`$, so the sign of $`C`$ agrees with the sign of $`x+y-1`$.

For an even $`n`$, $`\tau_n`$ has every marginal equal to $`I/2`$ and

```math
D_{\mathrm{rel}}\!\left(\tau_n\middle\|(I/2)^{\otimes n}\right)=n-\log_2 d_n .
```

Here $`D_{\mathrm{rel}}`$ denotes quantum relative entropy in bits. After applying $`\Gamma_D^{\otimes n}`$ or its complement, the entropy defect from the corresponding product output equals the relative entropy to that product, since the individual marginals are unchanged. Data processing bounds either entropy defect between zero and $`n-\log_2 d_n`$. Thus

```math
R_n^{(0)}(x,y)\ \ge\
 \max\!\left\{0,C(x,y)-\frac{n-\log_2 d_n}{n}\right\}.
```

### A ceiling for every block length

Suppose $`x+y\ge1`$. For a code using $`k`$ known coherence blocks, let $`N=kn`$ be the total number of slots. Draw one Haar-random right rotation for the entire code and set $`V=I`$ throughout. Every constant rotation sequence is allowed, so a uniformly reliable code also works on this average. The averaged $`N`$-carrier channel is $`\Gamma_D^{\otimes N}\circ\mathcal T_N`$, where $`\mathcal T_N`$ is the collective rotation twirl over all $`N`$ slots. The twirl has a Stinespring environment $`W`$ of dimension

```math
r_N=\sum_{j\ \mathrm{available}}(2j+1)^2=O(N^3).
```

The Kraus operators for each sector depolarize one spin space, act as identity on its multiplicity space, and remove coherence with other sectors.

For any input, let $`\sigma`$ be its twirled state and let $`\beta`$ and $`\zeta`$ be the canonical physical output and complementary output on $`\sigma`$. Invariance under every collective spin rotation makes every single-slot marginal $`I/2`$ and fixes $`\sigma`$ under collective $`X`$. The same swap-filter map used for spin-zero inputs implements $`\beta\mapsto\zeta`$ and sends $`\Gamma_D(I/2)^{\otimes N}`$ to the complementary product. Relative-entropy data processing gives

```math
D_{\mathrm{rel}}\!\big(\beta\big\|\Gamma_D(I/2)^{\otimes N}\big)
\ \ge\
D_{\mathrm{rel}}\!\big(\zeta\big\|\Gamma_L(I/2)^{\otimes N}\big).
```

These relative entropies are the two entropy defects, so $`S(\beta)-S(\zeta)\le N C(x,y)`$. The full averaged channel's environment includes $`W`$ as well. The conditional-entropy bound $`S(W|E)\ge-\log_2 r_N`$ gives an upper bound of $`NC(x,y)+\log_2 r_N`$ on its coherent information for every input.

To apply this bound to an arbitrary encoder, send half of a maximally entangled state of Schmidt rank $`K`$. If the encoder has several Kraus operators, the final target-state overlap is the weighted mean of the overlaps in the normalized Kraus branches. At least one branch has overlap at least $`1-\varepsilon`$ whenever the full code does. The reference and physical input are jointly pure in that branch. After decoding, its output is within half trace distance $`\delta\le\sqrt{\varepsilon}`$ of the target state. Coherent information cannot increase during decoding, and continuity of conditional entropy gives

```math
(1-2\delta)\log_2 K
 -(1+\delta)h_2\!\left(\frac{\delta}{1+\delta}\right)
\ \le\ NC(x,y)+\log_2 r_N .
```

As $`k\to\infty`$ at fixed $`n`$, the overhead $`\log_2 r_N/N`$ vanishes. Thus $`Q_n(x,y)\le C(x,y)`$ for every $`n`$ when $`x+y\ge1`$. At $`x+y\le1`$ the two-coin proof already gives zero capacity. The ceiling concerns unrestricted encoders and decoders, including ones that use several coherence blocks jointly.

### Taking the coherence length to infinity

The spin-zero input deficit obeys $`n-\log_2 d_n=O(\log n)`$. For odd $`n`$, use the spin-zero code on $`n-1`$ slots and count the unused slot in the rate. The lower bound and the ceiling then yield

```math
\lim_{n\to\infty}Q_n(x,y)=\max\{0,C(x,y)\}.
```

For fixed spectrum, the rate gap to this limit is at most $`O(\log n/n)`$ by the spin-zero construction.

Capacity here first takes the number of blocks to infinity at fixed block length. The subsequent limit increases the number of slots sharing a single filter. The limiting converse remains valid when $`x>1/2>y`$ or $`y>1/2>x`$, where the physical single-carrier channel can be neither degradable nor antidegradable.

The [within-block drift analysis](drift.md) gives error bounds and a positive-rate construction when the filter varies slightly across slots.

## Sources

- Bartlett, Rudolph and Spekkens established near-unit-rate quantum communication under a collective unknown unitary. [Phys. Rev. Lett. 91, 027901 (2003)](https://doi.org/10.1103/PhysRevLett.91.027901)
- Migdał and Banaszek established exact protection of spin-zero information from the loss of one particle under collective unitary rotations. [arXiv:1107.3786](https://arxiv.org/abs/1107.3786)
- Filippov analyzed the generalized erasure channel with state-dependent loss, including degradability and superadditivity for a specified polarization-dependent filter. [J. Phys. A 54, 255301 (2021)](https://doi.org/10.1088/1751-8121/abfd61)
- Ahlswede, Bjelaković, Boche and Nötzel supplied the arbitrarily varying quantum channel framework, including a regularized capacity formula and a calculation for state-independent erasure channels. [arXiv:1010.0418](https://arxiv.org/abs/1010.0418)
- Devetak and Devetak–Shor give the coherent-information coding theorem and its degradable-channel specialization. [arXiv:quant-ph/0304127](https://arxiv.org/abs/quant-ph/0304127) · [arXiv:quant-ph/0311131](https://arxiv.org/abs/quant-ph/0311131)
- Winter gives the dimension-dependent continuity bound for conditional entropy used in the converse. [arXiv:1507.07775](https://arxiv.org/abs/1507.07775)

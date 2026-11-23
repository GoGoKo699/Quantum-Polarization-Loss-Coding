# A fixed Schur receiver

## Encode across distinguishable carriers

For an even block of $`n`$ carriers, encode into its total spin-zero subspace $`\mathcal C_n`$. Under a Schur transform on $`r`$ carriers,

```math
(\mathbb C^2)^{\otimes r}=
 \bigoplus_j V_{r,j}\otimes M_{r,j},\qquad
\dim V_{r,j}=2j+1,
\qquad
m(r,2j)=\binom r{r/2-j}-\binom r{r/2-j-1}.
```

An angle or axis changes the spin factor $`V_{r,j}`$. The multiplicity space $`M_{r,j}`$ records the different ways to couple the carriers to that spin. Tensor powers of a common two-by-two matrix preserve this decomposition and act as the identity on multiplicities. This follows from commutation with permutations and extends to singular matrices by continuity. The code dimension is the Catalan number $`M_n=\binom{n}{n/2}/(n/2+1)`$.

On four carriers the code encodes a qubit. First couple carriers 1 and 2 and carriers 3 and 4. The first basis state is the product of the two pair singlets. The second couples two pair triplets to zero total spin:

```math
|0_L\rangle=|s\rangle_{12}|s\rangle_{34},\qquad
|1_L\rangle=
 \frac{|t_+\rangle|t_-\rangle-|t_0\rangle|t_0\rangle+
             |t_-\rangle|t_+\rangle}{\sqrt{3}}.
```

Here $`|s\rangle=(|01\rangle-|10\rangle)/\sqrt 2`$, and the triplets are $`|00\rangle`$, $`(|01\rangle+|10\rangle)/\sqrt 2`$, and $`|11\rangle`$. A fixed inverse Schur transform and a spin-zero register can also prepare the encoding.

## Decode after the loss flag

For a labeled split into survivors $`S`$ and losses $`L`$, a spin-zero block pairs equal spins on the two sides. Its natural cut coordinates are

```math
\mathcal C_n \simeq
 \bigoplus_j M_{S,j}\otimes M_{L,j}\otimes\mathrm{span}\{|\Omega_j\rangle\},
\qquad
|\Omega_j\rangle=
 \frac{1}{\sqrt{2j+1}}\sum_{m=-j}^{j}(-1)^{j-m}|j,m\rangle|j,-m\rangle.
```

Let $`P_{S,j}`$ project onto this summand and let $`W_{S,j}`$ identify it with the pair of multiplicities. The input unitary in the common filter is collective and therefore acts on $`\mathcal C_n`$ only by a scalar phase. The surviving and lost filters modify the one vector $`|\Omega_j\rangle`$ in each summand. Their squared norm multiplier, denoted $`w_{s,l,j}`$, depends only on the transmissivities and the sizes $`s=|S|`$ and $`l=|L|`$. The surviving output orientation acts only on the spin gauge.

The decoder reads the survival mask, applies the Schur transform to the surviving carriers, records $`j`$, and discards the spin gauge. Its two reduced output marginals for input $`\rho`$ are

```math
\begin{aligned}
\Phi_n(\rho)
 &=\bigoplus_{S,j} w_{s,l,j}\,
  \mathrm{Tr}_{M_{L,j}}\!\left(W_{S,j}P_{S,j}\rho P_{S,j}W_{S,j}^\dagger\right),\\
\Phi_n^c(\rho)
 &=\bigoplus_{S,j} w_{s,l,j}\,
  \mathrm{Tr}_{M_{S,j}}\!\left(W_{S,j}P_{S,j}\rho P_{S,j}W_{S,j}^\dagger\right).
\end{aligned}
```

Distinct $`j`$ sectors are orthogonal on both sides, and the same loss flag is available to each. For a fixed $`(S,j)`$, the joint state on gauges is pure and independent of the logical input. Discarding both gauges therefore subtracts the same entropy from both marginals and leaves coherent information unchanged. The reduced marginals are implemented together by the isometry with orthogonal copied flags and branch maps $`\sqrt{w_{s,l,j}}W_{S,j}P_{S,j}`$. This also establishes the channel identity with any reference entangled with the input. The outer quantum code sees the same channel on every block.

## Which four-carrier branches preserve information?

With three survivors, the receiver has a spin-half multiplicity of dimension two and the lost carrier has multiplicity one. With four survivors, the receiver has the original spin-zero multiplicity. Both cases pass the qubit to the receiver. Zero or one survivor passes the qubit to the environment.

With two survivors, both sides can measure the same singlet-versus-triplet tag. Each of its two possible multiplicities has dimension one. For the cut $`12\mid34`$, the logical basis above shows exactly how the tag can reveal a classical property of the input. It is available to both sides and makes zero contribution to the difference of their entropies. Declaring the branch to be a full qubit erasure discards the receiver's tag while crediting the full lost qubit in the ordinary erasure benchmark.

Let $`p_B`$ denote the total probability of three or four survivors and let $`p_E`$ denote zero or one survivor. They are independent of the logical state:

```math
p_B=2xy(x+y)-3x^2y^2,\qquad
p_E=2(1-x)(1-y)(2-x-y)-3(1-x)^2(1-y)^2.
```

Their difference is $`(x+y-1)(1+x+y-2xy)`$. At $`x=0.8,\ y=0.4`$, they are $`0.4608`$ and $`0.1488`$, respectively. The positive difference gives $`0.312`$ logical qubits per four-carrier block, or $`0.078`$ per carrier. Only crediting the first probability would turn this example into an ordinary erasure channel with transmission below one half. The [capacity proof](capacity.md) derives the exact coherent-information formula and identifies where the finite singlet rate is optimal.

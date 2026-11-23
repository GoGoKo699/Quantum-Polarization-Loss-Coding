# Numerical verification

From the repository root, run the following with Python 3 and NumPy installed.

```sh
python3 verification/verify.py
```

The script enumerates the spin-sector distribution of the uniform singlet for even blocks through 128 carriers. At $x=0.8$ and $y=0.4$, it gives $0.078$ qubits per emitted carrier for the four-carrier block and a long-coherence limit of about $0.22647$. It also checks that equal polarization survival gives the binomial loss law and that coherent information vanishes on $x+y=1$.

An independent calculation constructs the four-qubit singlet projector from swaps and applies the filter directly for every survival pattern. The script compares spin weights, entropies, and gauge-independent permutation moments across twelve seeded polarization orientations. The two-survivor check verifies that two orthogonal singlet inputs produce different public spin tags. The operator check applies the degrading filter to the four matrix units of the encoded qubit and compares its output with the direct complementary channel. The script also checks the coin-conditional antidegrading contractions at representative spectra at and below the threshold, including singular endpoints.

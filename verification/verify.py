"""Check finite singlet-code rates against direct four-qubit calculations."""

from itertools import combinations, permutations
from math import comb, fsum, log2

import numpy as np


ATOL = 1e-12
X = np.array([[0.0, 1.0], [1.0, 0.0]])


def spin_multiplicity(carriers, twice_spin):
    """Dimension of the spin multiplicity space, indexed by twice the spin."""
    if not 0 <= twice_spin <= carriers or (carriers - twice_spin) % 2:
        return 0
    lower = (carriers - twice_spin) // 2
    return comb(carriers, lower) - (comb(carriers, lower - 1) if lower else 0)


def finite_spin_distribution(n, x, y):
    """Return (survivor count, twice-spin) probabilities for the uniform singlet."""
    if n < 2 or n % 2:
        raise ValueError("The singlet calculation needs a positive even block size")
    if not 0 <= x <= 1 or not 0 <= y <= 1:
        raise ValueError("Survival probabilities must lie in [0, 1]")
    singlet_dim = spin_multiplicity(n, 0)
    probabilities = {}
    for s in range(n + 1):
        lost = n - s
        for t in range(s % 2, min(s, lost) + 1, 2):
            gauge_trace = fsum(
                (x * (1 - y)) ** (t - m) * (y * (1 - x)) ** m
                for m in range(t + 1)
            ) / (t + 1)
            weight = (x * y) ** ((s - t) // 2)
            weight *= ((1 - x) * (1 - y)) ** ((lost - t) // 2) * gauge_trace
            degeneracy = comb(n, s) * spin_multiplicity(s, t) * spin_multiplicity(lost, t)
            probabilities[s, t] = degeneracy / singlet_dim * weight
    return probabilities


def finite_rate(n, probabilities):
    """Signed uniform-singlet coherent information per emitted carrier."""
    return fsum(
        weight * log2(spin_multiplicity(s, t) / spin_multiplicity(n - s, t))
        for (s, t), weight in probabilities.items()
    ) / n


def entropy(probabilities):
    return -fsum(p * log2(p) for p in probabilities if p > 0)


def long_coherence_value(x, y):
    """Signed one-carrier coherent information at the maximally mixed input."""
    return entropy((x / 2, y / 2, 1 - (x + y) / 2)) - entropy(
        ((1 - x) / 2, (1 - y) / 2, (x + y) / 2)
    )


def tensor_power(matrix, exponent):
    result = np.ones((1, 1))
    for _ in range(exponent):
        result = np.kron(result, matrix)
    return result


def permute_operator(operator, order):
    n = len(order)
    axes = tuple(order) + tuple(n + index for index in order)
    return operator.reshape((2,) * (2 * n)).transpose(axes).reshape(operator.shape)


def permutation_matrix(order):
    dim = 2 ** len(order)
    return np.eye(dim).reshape((2,) * len(order) + (dim,)).transpose(
        tuple(order) + (len(order),)
    ).reshape(dim, dim)


def spin_projectors(n):
    """Construct projectors by diagonalizing J² using two-carrier swaps."""
    spin_squared = np.eye(2**n) * (n * (4 - n) / 4)
    for first, second in combinations(range(n), 2):
        swap = list(range(n))
        swap[first], swap[second] = swap[second], swap[first]
        spin_squared += permutation_matrix(swap)
    eigenvalues, eigenvectors = np.linalg.eigh(spin_squared)
    result = {}
    for t in range(n % 2, n + 1, 2):
        basis = eigenvectors[:, np.isclose(eigenvalues, t * (t + 2) / 4)]
        assert basis.shape[1] == (t + 1) * spin_multiplicity(n, t)
        result[t] = basis @ basis.conj().T
    return result


def physical_marginals(rho, receive, lose, n):
    """Apply the local Stinespring filters and trace each cut in both directions."""
    bob, environment = {}, {}
    for s in range(n + 1):
        filt = np.kron(tensor_power(receive, s), tensor_power(lose, n - s))
        for survivors in combinations(range(n), s):
            lost = tuple(index for index in range(n) if index not in survivors)
            joint = filt @ permute_operator(rho, survivors + lost) @ filt.conj().T
            cut = joint.reshape(2**s, 2 ** (n - s), 2**s, 2 ** (n - s))
            bob[survivors] = np.trace(cut, axis1=1, axis2=3)
            environment[lost] = np.trace(cut, axis1=0, axis2=2)
    return bob, environment


def postfilter_marginal(blocks, receive, lose):
    """Apply another flagged filter to each carrier present in a marginal."""
    result = {key: np.zeros_like(block, dtype=complex) for key, block in blocks.items()}
    for indices, block in blocks.items():
        survivors, _ = physical_marginals(block, receive, lose, len(indices))
        for local, subblock in survivors.items():
            original = tuple(indices[index] for index in local)
            result[original] += subblock
    return result


def direct_spin_distribution(blocks, projectors):
    result = {}
    for indices, block in blocks.items():
        s = len(indices)
        for t, projector in projectors[s].items():
            result[s, t] = result.get((s, t), 0.0) + np.trace(projector @ block).real
    return result


def marginal_entropy(blocks):
    return fsum(entropy(np.linalg.eigvalsh(block)) for block in blocks.values())


def random_unitary(rng):
    sample = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))
    unitary, triangular = np.linalg.qr(sample)
    phases = np.diag(triangular) / np.abs(np.diag(triangular))
    return unitary * phases


def check_gauge_blind_blocks(canonical, rotated, operators):
    # Permutations span the collective-rotation commutant for a fixed live set.
    for key, block in canonical.items():
        difference = rotated[key] - block
        moments = [np.trace(operator @ difference) for operator in operators[len(key)]]
        np.testing.assert_allclose(moments, 0.0, atol=ATOL, rtol=0)


def check_four_carriers(x, y):
    projectors = [spin_projectors(n) for n in range(5)]
    rho = projectors[4][0] / spin_multiplicity(4, 0)
    d = np.diag(np.sqrt([x, y]))
    b = np.diag(np.sqrt([1 - x, 1 - y]))
    canonical_bob, canonical_eve = physical_marginals(rho, d, b, 4)
    expected = finite_spin_distribution(4, x, y)
    expected_rate = (x + y - 1) * (1 + x + y - 2 * x * y) / 4
    permutations_by_size = [
        [permutation_matrix(order) for order in permutations(range(s))]
        for s in range(5)
    ]
    rng = np.random.default_rng(1327)
    for _ in range(12):
        u, v = random_unitary(rng), random_unitary(rng)
        bob, eve = physical_marginals(rho, v @ d @ u, u.conj().T @ b @ u, 4)
        check_gauge_blind_blocks(canonical_bob, bob, permutations_by_size)
        check_gauge_blind_blocks(canonical_eve, eve, permutations_by_size)
        for blocks, reverse in ((bob, False), (eve, True)):
            actual = direct_spin_distribution(blocks, projectors)
            wanted = {((4 - s if reverse else s), t): p for (s, t), p in expected.items()}
            for sector, probability in actual.items():
                np.testing.assert_allclose(probability, wanted.get(sector, 0), atol=ATOL, rtol=0)
            np.testing.assert_allclose(fsum(actual.values()), 1, atol=ATOL, rtol=0)
        actual_rate = (marginal_entropy(bob) - marginal_entropy(eve)) / 4
        np.testing.assert_allclose(actual_rate, expected_rate, atol=ATOL, rtol=0)

    # The two-by-two cut separates the two possible spin sectors of the code.
    singlet = np.array([0, 1, -1, 0]) / np.sqrt(2)
    two_dimers = np.kron(singlet, singlet)
    dimer_state = np.outer(two_dimers, two_dimers)
    other_state = projectors[4][0] - dimer_state
    for state, expected_spin in ((dimer_state, 0), (other_state, 2)):
        bob, _ = physical_marginals(state, d, b, 4)
        cut = bob[0, 1]
        assert np.trace(cut).real > 0
        wrong_spin = np.trace(projectors[2][2 - expected_spin] @ cut)
        np.testing.assert_allclose(wrong_spin, 0, atol=ATOL, rtol=0)

    # The same degradation mapping works on every logical matrix element.
    eigenvalues, vectors = np.linalg.eigh(projectors[4][0])
    code_basis = vectors[:, np.isclose(eigenvalues, 1)]
    ratios = np.array([(1 - y) / x, (1 - x) / y])
    post_receive = X @ np.diag(np.sqrt(ratios))
    post_lose = np.diag(np.sqrt(1 - ratios))
    for row in code_basis.T:
        for column in code_basis.T:
            operator = np.outer(row, column.conj())
            bob, eve = physical_marginals(operator, d, b, 4)
            degraded = postfilter_marginal(bob, post_receive, post_lose)
            for key, block in eve.items():
                np.testing.assert_allclose(degraded[key], block, atol=ATOL, rtol=0)



def check_two_survivor_effects(x, y):
    """Compare each tag and mask effect with the physical channel on matrix units."""
    singlet = np.array([0, 1, -1, 0]) / np.sqrt(2)
    dimer = np.kron(singlet, singlet)
    triplet_up = np.array([1, 0, 0, 0])
    triplet_zero = np.array([0, 1, 1, 0]) / np.sqrt(2)
    triplet_down = np.array([0, 0, 0, 1])
    triplet_pair = (
        np.kron(triplet_up, triplet_down)
        - np.kron(triplet_zero, triplet_zero)
        + np.kron(triplet_down, triplet_up)
    ) / np.sqrt(3)
    code_basis = np.column_stack((dimer, triplet_pair))
    w0 = x * y * (1 - x) * (1 - y)
    w1 = w0 + (x - y) ** 2 / 3
    projectors = spin_projectors(2)
    two_survivor_effects = {}
    for survivors in combinations(range(4), 2):
        lost = tuple(index for index in range(4) if index not in survivors)
        pair_dimer = permutation_matrix(survivors + lost).T @ dimer
        logical_dimer = code_basis.conj().T @ pair_dimer
        singlet_effect = np.outer(logical_dimer, logical_dimer.conj())
        two_survivor_effects[survivors] = {
            0: w0 * singlet_effect, 2: w1 * (np.eye(2) - singlet_effect)
        }

    rng = np.random.default_rng(624)
    u, v = random_unitary(rng), random_unitary(rng)
    receive = v @ np.diag(np.sqrt([x, y])) @ u
    lose = u.conj().T @ np.diag(np.sqrt([1 - x, 1 - y])) @ u
    for i, row in enumerate(code_basis.T):
        for j, column in enumerate(code_basis.T):
            operator = np.outer(row, column.conj())
            bob, _ = physical_marginals(operator, receive, lose, 4)
            total = 0.0j
            for survivors, effects in two_survivor_effects.items():
                block = bob[survivors]
                for twice_spin, effect in effects.items():
                    actual = np.trace(projectors[twice_spin] @ block)
                    np.testing.assert_allclose(actual, effect[j, i], atol=ATOL, rtol=0)
                mask_entry = (effects[0] + effects[2])[j, i]
                np.testing.assert_allclose(
                    np.trace(block), mask_entry, atol=ATOL, rtol=0
                )
                total += mask_entry
            np.testing.assert_allclose(
                total, 3 * (w0 + w1) * (i == j), atol=ATOL, rtol=0
            )


def check_subthreshold_postfilter(x, y):
    """Check both coin-conditional antidegrading filters on their input support."""
    d = np.diag(np.sqrt([x, y]))
    b = np.diag(np.sqrt([1 - x, 1 - y]))
    for coin in (np.eye(2), X):
        eve_live = coin @ b @ coin
        opposite_bob = d @ X @ coin
        post_receive = opposite_bob @ np.linalg.pinv(eve_live)
        residual = np.eye(2) - post_receive.conj().T @ post_receive
        assert np.linalg.eigvalsh(residual).min() >= -ATOL
        np.testing.assert_allclose(post_receive @ eve_live, opposite_bob, atol=ATOL, rtol=0)


def main():
    x, y = 0.8, 0.4
    print(" n   normalization    qubits per carrier")
    for n in (2, 4, 6, 8, 16, 32, 64, 128):
        probabilities = finite_spin_distribution(n, x, y)
        normalization = fsum(probabilities.values())
        rate = finite_rate(n, probabilities)
        np.testing.assert_allclose(normalization, 1, atol=ATOL, rtol=0)
        limit = long_coherence_value(x, y)
        deficit = (n - log2(spin_multiplicity(n, 0))) / n
        assert limit - deficit - ATOL <= rate <= limit + ATOL
        print(f"{n:3d}  {normalization:13.10f}    {rate:17.10f}")

    four = finite_spin_distribution(4, x, y)
    bob_probability = fsum(p for (s, _), p in four.items() if s >= 3)
    eve_probability = fsum(p for (s, _), p in four.items() if s <= 1)
    np.testing.assert_allclose([bob_probability, eve_probability], [0.4608, 0.1488], atol=ATOL, rtol=0)
    check_four_carriers(x, y)
    for a, b in ((x, y), (0.490, 0.509), (0.5, 0.5), (1.0, 0.3), (0.0, 0.3)):
        check_two_survivor_effects(a, b)
    for a, b in ((0.6, 0.3), (0.8, 0.2), (1.0, 0.0), (0.0, 0.0)):
        check_subthreshold_postfilter(a, b)

    for n in (2, 4, 8, 16):
        for p in (0.0, 0.3, 0.5, 0.7, 1.0):
            distribution = finite_spin_distribution(n, p, p)
            for s in range(n + 1):
                observed = fsum(weight for (size, _), weight in distribution.items() if size == s)
                binomial = comb(n, s) * p**s * (1 - p) ** (n - s)
                np.testing.assert_allclose(observed, binomial, atol=ATOL, rtol=0)
            np.testing.assert_allclose(long_coherence_value(p, p), 2 * p - 1, atol=ATOL, rtol=0)
        for a in (0.0, 0.2, 0.5, 0.8, 1.0):
            threshold = finite_spin_distribution(n, a, 1 - a)
            np.testing.assert_allclose(finite_rate(n, threshold), 0, atol=ATOL, rtol=0)

    print(f"Four-carrier receiver/environment branches: {bob_probability:.4f}, {eve_probability:.4f}")
    print(f"Long-coherence limit: {long_coherence_value(x, y):.10f} qubits per carrier")
    print("Direct matrices, spin weights, tag and mask effects, entropy, filters, and boundary checks passed.")


if __name__ == "__main__":
    main()

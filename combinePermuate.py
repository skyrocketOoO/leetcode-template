

def permutation_repetition(n: int, k: int) -> int:
    return n ** k

def permutation_without_repetition(n: int, k: int) -> int:
    ans = 1
    for choice in range(n, n-k, -1):
        ans *= choice
    return ans

def combination_repetition(n: int, k: int) -> int:
    ans = 1
    for i in range(n, n + k):
        ans *= i
    
    for i in range(1, k+1):
        ans //= i
    return ans
        
def combination_without_repetition(n: int, k: int) -> int:
    ans = 1
    for choice in range(n, n-k, -1):
        ans *= choice
    
    for arrangement in range(1, k+1):
        ans //= arrangement
    return ans

if __name__ == "__main__":
    n = 5  # Replace with the desired value of n
    k = 3  # Replace with the desired value of k

    # Permutations with repetition
    perm_rep = permutation_repetition(n, k)
    print(f"Permutations with repetition (n={n}, k={k}): {perm_rep}")

    # Permutations without repetition
    perm_no_rep = permutation_without_repetition(n, k)
    print(f"Permutations without repetition (n={n}, k={k}): {perm_no_rep}")

    # Combinations with repetition
    comb_rep = combination_repetition(n, k)
    print(f"Combinations with repetition (n={n}, k={k}): {comb_rep}")

    # Combinations without repetition
    comb_no_rep = combination_without_repetition(n, k)
    print(f"Combinations without repetition (n={n}, k={k}): {comb_no_rep}")

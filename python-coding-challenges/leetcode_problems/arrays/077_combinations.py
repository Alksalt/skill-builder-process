from itertools import combinations

def combine_easy(n: int, k: int) -> list[list[int]]:
    result = []
    for comb in combinations(range(1, n +1), k):
        result.append(list(comb))
    return result



# --- Runnable examples ---
if __name__ == "__main__":
    # Example 1
    n1, k1 = 4, 2
    print("Example 1:", combine(n1, k1))  # Expected (order can vary): [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

    # Example 2
    n2, k2 = 1, 1
    print("Example 2:", combine(n2, k2))  # Expected: [[1]]

    # Example 3
    n3, k3 = 5, 3
    print("Example 3:", combine(n3, k3))  # Expected (order can vary): combinations of 3 from [1..5]
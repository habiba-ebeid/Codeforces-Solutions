"""
Problem: Even Odds (318A)
Codeforces Submission ID: 388860661
Author: habebaabdelrahem4
"""

"""
Problem:318A. Even Odds (Codeforces)
Approach: Mathematical O(1) calculation. Partition the range [1, n] into odds and evens,
          then compute the k-th number directly based on whether k falls into odds or evens.
Time Complexity: O(1)
Space Complexity: O(1)
Author: Habiba
"""

def solve() -> None:
    n, k = map(int, input().split())

    # Count of odd numbers in range [1, n]
    total_odds = (n + 1) // 2

    # If k is within the odd partition
    if k <= total_odds:
        print(2 * k - 1)
    else:
        # Shift index to find the corresponding even number
        even_index = k - total_odds
        print(2 * even_index)

if __name__ == "__main__":
    solve()
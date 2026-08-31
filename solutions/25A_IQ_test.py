"""
Problem: IQ test (25A)
Codeforces Submission ID: 388972290
Author: habebaabdelrahem4
"""

"""
Problem: 25A. IQ test (Codeforces)
Approach: Map numbers to their parity (0 for even, 1 for odd). 
          Find the 1-based index of the unique parity that appears only once.
Time Complexity: O(n)
Space Complexity: O(n)
Author: Habiba
"""

def solve() -> None:
    input()  # Ignore n
    numbers = list(map(int, input().split()))

    # Extract parity (0 for even, 1 for odd)
    parities = [x % 2 for x in numbers]

    # Find which parity is the odd-one-out (appears only once)
    target_parity = 1 if parities.count(1) == 1 else 0

    # Output 1-based index
    print(parities.index(target_parity) + 1)

if __name__ == "__main__":
    solve()
"""
Problem: Twins (160A)
Codeforces Submission ID: 388860601
Author: habebaabdelrahem4
"""

"""
Problem: A. Twins (Codeforces)
Approach: Sort coins descending and use prefix slicing to find the minimum number 
          of largest coins whose sum strictly exceeds half of the total sum.
Time Complexity: O(n log n)
Space Complexity: O(n)
Author: Habiba
"""

def solve() -> None:
    input()
    coins = sorted(map(int, input().split()), reverse=True)
    half_sum = sum(coins) / 2

    for count in range(1, len(coins) + 1):
        if sum(coins[:count]) > half_sum:
            print(count)
            break

if __name__ == "__main__":
    solve()
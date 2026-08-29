"""
Problem: Vanya and Lanterns (492B)
Codeforces Submission ID: 388859753
Author: habebaabdelrahem4
"""

"""
Problem: 492B. Vanya and Lanterns (Codeforces)
Approach: Find maximum gap between adjacent sorted lanterns (/ 2) vs boundaries (0, l).
Author: Habiba
"""

def solve() -> None:
    n, l = map(int, input().split())
    lanterns = sorted(map(int, input().split()))

    # Max gap between adjacent lanterns (defaults to 0 if n == 1)
    max_between = max((lanterns[i + 1] - lanterns[i] for i in range(n - 1)), default=0) / 2.0

    # Distance to boundaries (start at 0 and end at l)
    start_dist = lanterns[0]
    end_dist = l - lanterns[-1]

    # Required radius is the maximum of all critical distances
    print(f"{max(start_dist, end_dist, max_between):.10f}")

if __name__ == "__main__":
    solve()
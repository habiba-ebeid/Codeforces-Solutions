"""
Problem: Xenia and Ringroad (339B)
Codeforces Submission ID: 389247132
Author: habebaabdelrahem4
"""

"""
Codeforces - 339B: Xenia and Ringroad
 Using modular arithmetic to handle circular steps in O(1) per task.
By: Habiba
"""

def solve() -> None:
    houses_count, _ = map(int, input().split())
    errands = list(map(int, input().split()))

    current_house = 1
    total_steps = 0

    for next_house in errands:
        # Python handles negative modulo natively, wrapping around the ringroad automatically
        total_steps += (next_house - current_house) % houses_count
        current_house = next_house

    print(total_steps)

if __name__ == "__main__":
    solve()
"""
Problem: Kefa and First Steps (580A)
Codeforces Submission ID: 389432786
Author: habebaabdelrahem4
"""

"""
Codeforces - 580A: Kefa and First Steps
By: Habiba
"""

def solve() -> None:
    days_count = int(input())
    earnings = list(map(int, input().split()))

    current_streak = 1
    best_streak = 1

    for day in range(1, days_count):
        if earnings[day] >= earnings[day - 1]:
            current_streak += 1
            if current_streak > best_streak:
                best_streak = current_streak
        else:
            current_streak = 1

    print(best_streak)

if __name__ == "__main__":
    solve()
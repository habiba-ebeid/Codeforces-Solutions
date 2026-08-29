"""
Problem: Taxi (158B)
Codeforces Submission ID: 388860725
Author: habebaabdelrahem4
"""

"""
Problem: B. Taxi (Codeforces)
Approach: Greedy strategy - allocate cars for larger friend groups first, 
          then pack singles into leftover seats.
Author: Habiba
"""

def solve() -> None:
    total_groups = int(input())
    friend_groups = list(map(int, input().split()))

    # Count of each group size
    singles = friend_groups.count(1)
    pairs = friend_groups.count(2)
    trios = friend_groups.count(3)
    fours = friend_groups.count(4)

    cars_needed = 0

    # 1. Groups of 4 occupy an entire car
    cars_needed += fours

    # 2. Trios get their own car + take 1 single if available
    cars_needed += trios
    singles = max(0, singles - trios)

    # 3. Pair up two duos into one car
    cars_needed += pairs // 2
    if pairs % 2 == 1:
        cars_needed += 1
        singles = max(0, singles - 2)

    # 4. Pack remaining singles (up to 4 per car)
    if singles > 0:
        cars_needed += (singles + 3) // 4

    print(cars_needed)

if __name__ == "__main__":
    solve()
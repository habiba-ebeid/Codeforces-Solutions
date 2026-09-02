"""
Problem: Dragons (230A)
Codeforces Submission ID: 389162457
Author: habebaabdelrahem4
"""

"""
Problem: 230A. Dragons (Codeforces)
Approach: Sort dragons ascending by required combat power; farm easier bonuses first.
Author: Habiba
"""

def solve() -> None:
    current_hp, n = map(int, input().split())
    fights = sorted(tuple(map(int, input().split())) for _ in range(n))

    for monster_hp, bonus in fights:
        if current_hp <= monster_hp:
            print("NO")
            break
        current_hp += bonus
    else:
        print("YES")

if __name__ == "__main__":
    solve()
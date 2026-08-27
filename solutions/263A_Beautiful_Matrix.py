"""
Problem: Beautiful Matrix (263A)
Codeforces Submission ID: 388414949
Author: habebaabdelrahem4
"""

for r in range(1, 6):
    row = list(map(int, input().split()))
    if 1 in row:
        c = row.index(1) + 1
        moves = abs(r - 3) + abs(c - 3)
        print(moves)
        break
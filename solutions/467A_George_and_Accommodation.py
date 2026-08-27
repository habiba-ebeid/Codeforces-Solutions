"""
Problem: George and Accommodation (467A)
Codeforces Submission ID: 388532362
Author: habebaabdelrahem4
"""

n = int(input())

count = 0

for _ in range(n):
    p, q = map(int, input().split())
    if q - p >= 2:
        count += 1

print(count)
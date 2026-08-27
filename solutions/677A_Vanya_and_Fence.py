"""
Problem: Vanya and Fence (677A)
Codeforces Submission ID: 388531229
Author: habebaabdelrahem4
"""

n, h = map(int, input().split())
heights = list(map(int, input().split()))

total_width = 0

for a in heights:
    if a > h:
        total_width += 2
    else:
        total_width += 1

print(total_width)
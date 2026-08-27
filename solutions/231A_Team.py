"""
Problem: Team (231A)
Codeforces Submission ID: 388412588
Author: habebaabdelrahem4
"""

n = int(input())
count = 0

for _ in range(n):
    p, v, t = input().split()
    p = int(p)
    v = int(v)
    t = int(t)
   
    if (p == 1 and v == 1) or (p == 1 and t == 1) or (v == 1 and t == 1):
        count += 1

print(count)
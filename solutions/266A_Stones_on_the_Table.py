"""
Problem: Stones on the Table (266A)
Codeforces Submission ID: 388416684
Author: habebaabdelrahem4
"""

n = int(input())
s = input().strip()

count = 0

for i in range(n - 1):
    if s[i] == s[i + 1]:
        count += 1

print(count)
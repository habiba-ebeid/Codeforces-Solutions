"""
Problem: Petya and Strings (112A)
Codeforces Submission ID: 388415098
Author: habebaabdelrahem4
"""

s1 = input().lower()
s2 = input().lower()

if s1 < s2:
    print(-1)
elif s1 > s2:
    print(1)
else:
    print(0)
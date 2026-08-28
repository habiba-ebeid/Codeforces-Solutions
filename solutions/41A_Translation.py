"""
Problem: Translation (41A)
Codeforces Submission ID: 388531728
Author: habebaabdelrahem4
"""

s = input().strip()
t = input().strip()

if s[::-1] == t:
    print("YES")
else:
    print("NO")
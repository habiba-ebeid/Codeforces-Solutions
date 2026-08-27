"""
Problem: Beautiful Year (271A)
Codeforces Submission ID: 388531395
Author: habebaabdelrahem4
"""

y = int(input())

while True:
    y += 1
    if len(set(str(y))) == 4:
        print(y)
        break
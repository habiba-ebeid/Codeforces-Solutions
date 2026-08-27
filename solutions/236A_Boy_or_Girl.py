"""
Problem: Boy or Girl (236A)
Codeforces Submission ID: 388415652
Author: habebaabdelrahem4
"""

s = input().strip()

distinct_count = len(set(s))

if distinct_count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
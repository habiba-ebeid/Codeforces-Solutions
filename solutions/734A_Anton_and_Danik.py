"""
Problem: Anton and Danik (734A)
Codeforces Submission ID: 388530893
Author: habebaabdelrahem4
"""

n = int(input())
s = input().strip()

anton_wins = s.count('A')
danik_wins = s.count('D')

if anton_wins > danik_wins:
    print("Anton")
elif danik_wins > anton_wins:
    print("Danik")
else:
    print("Friendship")
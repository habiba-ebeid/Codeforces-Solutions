"""
Problem: Bear and Big Brother (791A)
Codeforces Submission ID: 388416004
Author: habebaabdelrahem4
"""

a, b = map(int, input().split())

years = 0

while a <= b:
    a *= 3
    b *= 2
    years += 1

print(years)
"""
Problem: Word (59A)
Codeforces Submission ID: 388417468
Author: habebaabdelrahem4
"""

s = input().strip()

upper_count = 0
lower_count = 0

for char in s:
    if char.isupper():
        upper_count += 1
    else:
        lower_count += 1

if upper_count > lower_count:
    print(s.upper())
else:
    print(s.lower())
"""
Problem: String Task (118A)
Codeforces Submission ID: 388623034
Author: habebaabdelrahem4
"""

s = input().strip().lower()

vowels = "aoyeui"
result = []

for char in s:
    if char not in vowels:
        result.append('.' + char)

print(''.join(result))
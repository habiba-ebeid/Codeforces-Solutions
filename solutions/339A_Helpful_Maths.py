"""
Problem: Helpful Maths (339A)
Codeforces Submission ID: 388415775
Author: habebaabdelrahem4
"""

s = input().strip()

numbers = s.split('+')
numbers.sort()

ans = '+'.join(numbers)
print(ans)
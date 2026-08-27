"""
Problem: Nearly Lucky Number (110A)
Codeforces Submission ID: 388531058
Author: habebaabdelrahem4
"""

s = input().strip()

lucky_count = s.count('4') + s.count('7')

if lucky_count == 4 or lucky_count == 7:
    print("YES")
else:
    print("NO")
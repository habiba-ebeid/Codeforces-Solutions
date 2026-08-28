"""
Problem: Chat room (58A)
Codeforces Submission ID: 388624591
Author: habebaabdelrahem4
"""

s = input().strip()

target = "hello"
index = 0

for char in s:
    if char == target[index]:
        index += 1
        if index == len(target):
            break

if index == len(target):
    print("YES")
else:
    print("NO")
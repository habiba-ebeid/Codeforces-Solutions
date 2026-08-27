"""
Problem: Three Numbers on the Blackboard (2256A)
Codeforces Submission ID: 388314965
Author: habebaabdelrahem4
"""

t = int(input())
for _ in range(t):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    numbers = [a, b, c]
    numbers.sort()
    
    x = numbers[0]
    y = numbers[1]
    z = numbers[2]
    ans = min(z - x, y)
    print(ans)
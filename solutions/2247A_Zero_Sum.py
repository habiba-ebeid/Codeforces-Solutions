"""
Problem: Zero Sum (2247A)
Codeforces Submission ID: 388411206
Author: habebaabdelrahem4
"""

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        total_sum = sum(a)
        
        if total_sum % 4 == 0:
            print("YES")
        else:
            print("NO")

solve()
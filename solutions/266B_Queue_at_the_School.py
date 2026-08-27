"""
Problem: Queue at the School (266B)
Codeforces Submission ID: 388532195
Author: habebaabdelrahem4
"""

n, t = map(int, input().split())
s = input().strip()

for _ in range(t):
    s = s.replace("BG", "GB")

print(s)
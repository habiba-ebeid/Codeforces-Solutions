"""
Problem: Next Round (158A)
Codeforces Submission ID: 388413680
Author: habebaabdelrahem4
"""

n, k = map(int, input().split())
scores = list(map(int, input().split()))

target_score = scores[k - 1]
count = 0

for score in scores:
    if score >= target_score and score > 0:
        count += 1

print(count)
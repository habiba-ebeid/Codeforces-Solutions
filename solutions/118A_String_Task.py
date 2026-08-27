"""
Problem: String Task (118A)
Codeforces Submission ID: 388417264
Author: habebaabdelrahem4
"""

s = input().strip().lower()

vowels = "aoyeui"
result = ""

for char in s:
    if char not in vowels:
        result += "." + char

print(result)
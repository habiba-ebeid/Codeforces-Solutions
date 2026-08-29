"""
Problem: Registration System (4C)
Codeforces Submission ID: 388858945
Author: habebaabdelrahem4
"""

# Problem: C. Registration System
# Logic: Hash Map lookup to achieve O(1) time complexity per registration request.

def register_user(username: str, registry: dict) -> str:
    if username not in registry:
        registry[username] = 1
        return "OK"
    else:
        new_username = f"{username}{registry[username]}"
        registry[username] += 1
        return new_username

def solve():
    n = int(input())
    registry = {}
    
    for _ in range(n):
        username = input().strip()
        print(register_user(username, registry))

if __name__ == "__main__":
    solve()
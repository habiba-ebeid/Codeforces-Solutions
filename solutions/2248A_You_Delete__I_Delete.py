"""
Problem: You Delete, I Delete (2248A)
Codeforces Submission ID: 388410408
Author: habebaabdelrahem4
"""

def solve():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        
        alice_options = []
        for i in range(len(s)):
            if s[i] == '0':
                after_alice = s[:i] + s[i+1:]
                
                bob_options = []
                for j in range(len(after_alice)):
                    if after_alice[j] == '1':
                        bob_options.append(after_alice[:j] + after_alice[j+1:])
                
                alice_options.append(min(bob_options))
        
        print(max(alice_options))

solve()
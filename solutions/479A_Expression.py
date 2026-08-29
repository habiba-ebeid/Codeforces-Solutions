"""
Problem: Expression (479A)
Codeforces Submission ID: 388859342
Author: habebaabdelrahem4
"""

# Problem: 479A. Expression (Codeforces)
# Approach: Evaluate all 6 possible combinations of +, *, and brackets, then return the maximum.
# Author: Habiba

def get_max_expression(a: int, b: int, c: int) -> int:
    possibilities = [
        a + b + c,
        a * b * c,
        (a + b) * c,
        a * (b + c),
        a + (b * c),
        (a * b) + c
    ]
    return max(possibilities)

def solve() -> None:
    a: int = int(input())
    b: int = int(input())
    c: int = int(input())
    
    result: int = get_max_expression(a, b, c)
    print(result)

if __name__ == "__main__":
    solve()
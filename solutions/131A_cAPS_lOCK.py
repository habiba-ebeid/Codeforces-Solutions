"""
Problem: cAPS lOCK (131A)
Codeforces Submission ID: 389058324
Author: habebaabdelrahem4
"""

"""
Problem: A. cAPS lOCK (Codeforces)
Approach: Check if the word is fully uppercase or uppercase starting from index 1.
          If true, flip all letter cases using swapcase(); otherwise, leave untouched.
Author: Habiba
"""

def solve() -> None:
    word = input().strip()

    # Rule applies if all characters from the second character onwards are uppercase
    if len(word) == 1 or word[1:].isupper():
        print(word.swapcase())
    else:
        print(word)

if __name__ == "__main__":
    solve()
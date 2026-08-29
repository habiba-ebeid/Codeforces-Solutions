"""
Problem: Dubstep (208A)
Codeforces Submission ID: 388860365
Author: habebaabdelrahem4
"""

"""
Problem: 208A. Dubstep (Codeforces)
Approach: Replace "WUB" with spaces and split to filter out extra whitespace,
          then join the restored words with a single space.
Time Complexity: O(N) where N is the length of the remix string
Space Complexity: O(N)
Author: Habiba
"""

def solve() -> None:
    remix_track = input().strip()

    # Replace dubstep beats with whitespace, then extract clean lyrics
    original_words = remix_track.replace("WUB", " ").split()

    # Join the words back with single spaces
    print(" ".join(original_words))

if __name__ == "__main__":
    solve()
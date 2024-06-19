"""
Module: 1
Week: 2
HW: calculate levenshtein distance.
"""


def levenshtein_matrix(s, t):
    """
    Calculate the levenshtein distance between two strings using matrix. (2D array)
    """
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    return dp


if __name__ == "__main__":
    SOURCE = "yu"
    TARGET = "youu"
    print(levenshtein_matrix(SOURCE, TARGET)[len(SOURCE)][len(TARGET)])  # 1

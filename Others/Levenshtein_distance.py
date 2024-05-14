def Levenshtein(string_1, string_2):
    len_1, len_2 = len(string_1), len(string_2)
    dp = [[0 for _ in range(len_2 + 1)] for _ in range(len_1 + 1)]

    # Base case: when len_1 = 0 and len_2 = 0
    for j in range(len_2 + 1): dp[0][j] = j
    for i in range(len_1 + 1): dp[i][0] = i

    for i in range(1, len_1 + 1):
        for j in range(1, len_2 + 1):
            if string_1[i - 1] == string_2[j - 1]: dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j], # Insertion
                    dp[i][j-1], # Deletion
                    dp[i-1][j-1] # Replacement
                )
    return dp[len_1][len_2]

List_1 = ["Helo", "algorithm", "aboba", "tapok"]
List_2 = ["Hello", "rhythm", "bibaiboba", "topka"]
for i in range(len(List_1)):
    print(f"Levenshtein distance between {List_1[i]} and {List_2[i]} = {Levenshtein(List_1[i], List_2[i])}")

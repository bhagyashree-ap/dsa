class Solution:
    def numWays(self, words, target):
        
        M = 10**9 + 7
        L, T = len(words[0]), len(target)

        #count each letter at every position
        cnt = [[0] * 26 for _ in range(L)]
        
        for w in words:
            for i, ch in enumerate(w):
                cnt[i][ord(ch) - 97] += 1

        #dp[j] = ways to form target[:j]
        dp = [1] + [0] * T

        for i in range(L):
            #reverse to avoid reusing position i
            for j in range(T - 1, -1, -1):
                dp[j + 1] = (
                    dp[j + 1] + dp[j] * cnt[i][ord(target[j]) - 97]
                ) % M

        return dp[T]
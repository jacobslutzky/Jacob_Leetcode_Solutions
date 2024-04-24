class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        for start in range(len(s)+1):
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict:
                    dp[end] = dp[start]
        return dp[-1]

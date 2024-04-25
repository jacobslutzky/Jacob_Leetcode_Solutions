class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp = [[] for _ in range(target+1)]
        for num in candidates:
            if num < target+1:
                dp[num].append([num])
            for i in range(1, target+1):
                if i-num > 0:
                    for arr in dp[i-num]:
                        if arr:
                            dp[i].append(arr + [num])
          
        return dp[-1]

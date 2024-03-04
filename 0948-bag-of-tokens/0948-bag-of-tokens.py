class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        start = 0
        end = len(tokens)-1
        points = 0
        max_score = 0
        while start <= end:
            if tokens[start] <= power:
                power -= tokens[start]
                points +=1
                start+=1
            elif points > 0:
                power += tokens[end]
                points -= 1
                end -= 1
            else:
                start+=1
            max_score = max(max_score, points)
        return max_score
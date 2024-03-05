class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checkPossible(weight):
            i = 0
            curr_weight = 0
            for _ in range(days):
                curr_weight = 0
                while i < len(weights) and curr_weight+weights[i] <= weight:
                    curr_weight+=weights[i]
                    i+=1
                if i >= len(weights):
                    return True
            return False
            

        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = low + (high-low)//2
            if checkPossible(mid):
                high = mid
            else:
                low = mid + 1
        return low

        
    
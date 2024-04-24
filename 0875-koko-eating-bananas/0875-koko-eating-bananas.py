class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            mid = low + (high-low)//2
            curr_hour = 0
            curr_pile = 0
            while curr_hour < h and curr_pile < len(piles):
                curr_hour+= ceil(piles[curr_pile]/mid)
                if curr_hour <= h:
                    curr_pile+=1

            if curr_pile < len(piles):
                low = mid+1
            else:
                high = mid

        return low


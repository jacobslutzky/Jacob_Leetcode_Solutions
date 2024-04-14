class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        
        left_found = False
        right_found = False
        start = 0
        end = len(nums)-1
        while start <= end and (not left_found or not right_found):
            if not left_found:
                is_prime = True
                if nums[start] < 2:
                    is_prime = False
                for factor_x in range(2, int(nums[start]**(1/2))+1):
                    if nums[start] % factor_x == 0:
                        is_prime=False
                left_found = is_prime
                if not is_prime:
                    start+=1

            if not right_found:
                is_prime = True
                if nums[end] < 2:
                    is_prime = False
                for factor_y in range(2, int(nums[end]**(1/2))+1):
                    if nums[end] % factor_y == 0:
                        is_prime=False
                right_found = is_prime
                if not is_prime:
                    end-=1
        print(end)
        print(start)
        return end-start

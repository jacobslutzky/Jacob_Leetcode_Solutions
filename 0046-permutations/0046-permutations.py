class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        def get_perms(curr, nums):
            if not nums:
                output.append(curr)
                return
            for i in range(len(nums)):
                get_perms(curr + [nums[i]], nums[:i] + nums[i+1:])

        get_perms([], nums)
        return output

        
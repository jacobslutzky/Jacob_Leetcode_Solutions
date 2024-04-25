class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        def get_subsets(curr_subset, curr_nums):
            if not curr_nums:
                output.append(curr_subset)
                return

            i = 1
            while i < len(curr_nums) and curr_nums[i] == curr_nums[0]:
                i+=1
            get_subsets(curr_subset, curr_nums[i:])
            get_subsets(curr_subset+[curr_nums[0]], curr_nums[1:])
        get_subsets([],nums)
        return output
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        def create_subsets(curr, curr_nums):
            if not curr_nums:
                self.output.append(curr)
                return
            
            create_subsets(curr,curr_nums[1:])
            create_subsets(curr+[curr_nums[0]],curr_nums[1:])
        create_subsets([],nums)
        return self.output


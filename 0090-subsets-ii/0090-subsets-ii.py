class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        output = [[]]
        nums.sort()
        def backtrack(curr, subset):
            for i in range(len(subset)):
                if i == 0 or subset[i] != subset[i-1]:
                    output.append(curr+[subset[i]])
                    backtrack(curr + [subset[i]], subset[i+1:])
        
        backtrack([],nums)
        return output

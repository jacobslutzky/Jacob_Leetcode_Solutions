class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = [num for num in candidates if num <= target]
        candidates.sort()
        print(candidates)

        output=[]

        def get_combinations(curr, index):
            curr_sum = sum(curr)
            if curr_sum == target:
                output.append(curr)
                return
            if curr_sum  > target or index >= len(candidates):
                return

            get_combinations(curr + [candidates[index]], index+1)

            curr_num = index
            index+=1
            while index < len(candidates) and candidates[index] == candidates[curr_num]:
                index+=1
            get_combinations(curr, index)

        
        get_combinations([], 0)
        return output
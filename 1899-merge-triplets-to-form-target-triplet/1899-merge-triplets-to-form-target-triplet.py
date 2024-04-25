class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        

        index_one = [t for t in triplets if t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2]]
        index_two = [t for t in triplets if t[1] == target[1] and t[0] <= target[0] and t[2] <= target[2]]
        index_three = [t for t in triplets if t[2] == target[2] and t[0] <= target[0] and t[1] <= target[1]]

        if not index_one or not index_two or not index_three:
            return False
        return True
        
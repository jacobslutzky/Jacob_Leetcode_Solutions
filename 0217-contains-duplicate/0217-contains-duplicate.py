class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for num in nums:
            if num in d:
                return False
            else:
                d.add(num)
        return True

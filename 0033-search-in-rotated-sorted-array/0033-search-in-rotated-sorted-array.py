class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low < high:
            mid = low + (high-low)//2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid+1
        print(nums[low])
        if target > nums[len(nums)-1]:
            high = low
            low = 0
        else:
            high = len(nums)-1
        print(low)
        print(high)
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] < target:
                low = mid+1
            elif nums[mid] > target:
                high = mid-1
            else:
                return mid
        return -1
            
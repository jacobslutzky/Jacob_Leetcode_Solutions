class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        i = 0
        nums = list(num)
        if k >= len(nums):
            return "0"
        while k > 0:
            if i < len(nums)-1:
                if nums[i] > nums[i+1]:
                    nums.pop(i)
                    if i > 0:
                        i-=1
                    k-=1
                else:
                    i+=1
            elif i == len(nums)-1:
                nums.pop(i)
                i-=1
                k-=1
            else:
                break


        while len(nums) > 1 and nums[0] == "0":
            nums.pop(0)
        return "".join(nums)
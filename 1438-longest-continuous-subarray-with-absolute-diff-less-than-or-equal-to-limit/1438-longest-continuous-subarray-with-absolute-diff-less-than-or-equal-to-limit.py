class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        end = 0
        start = 0
        min_queue = [(nums[0],0)]
        max_queue = [(nums[0],0)]
        start = 0
        max_len = 0
        for end in range(1,len(nums)):
            while min_queue and nums[end] < min_queue[-1][0]:
                min_queue.pop()
            while max_queue and nums[end] > max_queue[-1][0]:
                max_queue.pop()
            min_queue.append((nums[end],end))
            max_queue.append((nums[end],end))
            while max_queue[0][0] - min_queue[0][0] > limit:
                if max_queue[0][1] < min_queue[0][1]:
                    element, index = max_queue.pop(0)
                    start = index+1
                else:
                    element, index = min_queue.pop(0)
                    start = index+1
            max_len = max(max_len,end-start+1)

        return max_len
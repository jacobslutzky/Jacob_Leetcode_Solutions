from heapq import heappush, heappop, heapify
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        i = 0
        j = 0

        nums1 = nums1[:k]
        nums2 = nums2[:k]
        heap = []
        for i in range(len(nums1)):
            heappush(heap,[nums1[i] + nums2[0],i,0])
        output = []
        while len(output) < k:
            summ, i, j = heappop(heap)
            output.append([nums1[i],nums2[j]])
            if j < len(nums2)-1:
                heappush(heap, [nums1[i] + nums2[j+1],i,j+1])
        
       
        return output
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        
        max_bucket = 0
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
            max_bucket = max(max_bucket, freqs[num])
        buckets = [[] for i in range(max_bucket+1)]
        for num in freqs:
            buckets[freqs[num]].append(num)
        
        output = []
        buckets = [bucket for bucket in buckets if bucket]
       
        for bucket in buckets[::-1]:
            for element in bucket:
                output.append(element)
                if len(output) >= k:
                    return output

        return output

            



        
                
                

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        
        longest = 0
        queue = []
        end = 0
        start = 0
        while end < len(s):
            while s[end] in d:
                first = queue.pop(0)
                del d[first]
            queue.append(s[end])
            d[s[end]] = 1
            if len(queue) > longest:
                longest = len(queue)
            end +=1
        return longest        
                


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # max_count = 0
        # for i in range(len(s)):
        #     d = [0]*26
        #     for j in range(i,len(s)):
        #         d[ord(s[j])-97] += 1
        #         if not [i for i in d if i > 0 and i < k]:
        #             max_count = max(max_count, j-i+1)

        def div_and_conq(s):
            if len(s) < k:
                return 0
            arr = [0]*26
            for i in range(len(s)):
                arr[ord(s[i])-97]+=1
            for i in range(len(s)):
                if arr[ord(s[i])-97] < k:
                    left  = div_and_conq(s[:i])
                    right = div_and_conq(s[i+1:])
                    return max(left, right)
            return len(s)

            
        return div_and_conq(s)

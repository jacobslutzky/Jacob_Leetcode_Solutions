class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        start = 0
        d = {s[0]: 1}
        curr_char = s[0]
        max_len = 1
        for end in range(1, len(s)):
            if s[end] not in d:
                d[s[end]] = 1
            else:
                d[s[end]] += 1
            if d[s[end]] > d[curr_char]:
                curr_char = s[end]
        
            while end-start+1 - d[curr_char] > k:
               
                d[s[start]] -= 1
                start+=1
                for i in d:
                    if d[i] > d[curr_char]:
                        curr_char = i
            
            max_len = max(max_len, end-start+1)
        return max_len

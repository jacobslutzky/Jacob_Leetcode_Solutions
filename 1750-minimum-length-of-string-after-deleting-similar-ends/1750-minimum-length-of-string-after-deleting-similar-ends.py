class Solution:
    def minimumLength(self, s: str) -> int:
        start = 0
        end = len(s)-1

        while start < end and s[start] == s[end]:
            while start < end and s[start] == s[start+1]:
                start+=1
            while end > start and s[end] == s[end-1]:
                end-=1
        
            start+=1
            end -=1
        return max(end-start+1,0)
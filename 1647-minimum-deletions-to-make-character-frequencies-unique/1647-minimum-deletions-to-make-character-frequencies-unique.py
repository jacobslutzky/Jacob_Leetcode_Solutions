class Solution:
    def minDeletions(self, s: str) -> int:
        arr = [0]*(len(s)+1)
        
        s = [x for x in s]
        s.sort()
        count = 1
        total_count = 0
        for i in range(0,len(s)):
            if i+1 < len(s) and s[i] == s[i+1]:
                count+=1
            else:
                while count > 0 and arr[count] != 0:
                    count-=1
                    total_count += 1
                arr[count] = 1
                count=1
        return total_count

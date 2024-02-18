class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        d = {}
        for char in s1:
            if char in d:
                d[char]+=1
            else:
                d[char] = 1
        
        for char in range(len(s1)):
            if s2[char] in d:
                d[s2[char]] -= 1
                if d[s2[char]] == 0:
                    del d[s2[char]]
            else:
                d[s2[char]] = -1
        if not d:
            return True

        for i in range(len(s2)-len(s1)):
            if s2[i] in d:
                d[s2[i]]+=1
                if d[s2[i]] == 0:
                    del d[s2[i]]
            else:
                d[s2[i]] = 1
            end = i+len(s1)
            if s2[end] in d:
                d[s2[end]] -= 1
                if d[s2[end]] == 0:
                    del d[s2[end]]
            else:
                d[s2[end]] = -1
            if not d:
                return True
        
        return False
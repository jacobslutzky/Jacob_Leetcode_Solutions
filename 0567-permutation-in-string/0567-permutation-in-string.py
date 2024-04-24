class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        window = {}

        if len(s1) > len(s2):
            return False
        
        for char in s1:
            if char in window:
                window[char] +=1
            else:
                window[char] = 1
        
        for char in s2[:len(s1)]:
            if char in window:
                window[char]-=1
                if window[char] == 0:
                    del window[char]
            else:
                window[char]=-1
        if not window:
            return True
        for i in range(len(s2)-len(s1)):
            start = s2[i]
            end = s2[i + len(s1)]
            if not window:
                return True
            if start in window:
                window[start] += 1
                if window[start] == 0:
                    del window[start]
            else:
                window[start] = 1
            if end in window:
                window[end] -= 1
                if window[end] == 0:
                    del window[end]
            else:
                window[end] = -1
            
            if not window:
                return True
        return False

class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        
        alph = [0]*26
        alph[ord(s[0])-97] = 1
        streak = 1
        for i in range(1, len(s)):
            if (ord(s[i-1])-96)%26 == ord(s[i])-97:
                streak+=1
            else:
                streak = 1
            alph[ord(s[i])-97] = max(alph[ord(s[i])-97], streak)
        return sum(alph)
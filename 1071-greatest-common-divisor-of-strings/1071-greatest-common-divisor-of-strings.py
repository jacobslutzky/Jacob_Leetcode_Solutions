class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        i = 0
        gcd = ""
        output = ""
        while i < min(len(str1),len(str2)) and str1[i] == str2[i]:
            gcd += str1[i]
            i+=1
            if len(str1) % i == 0 and len(str2) % i == 0:
                output = gcd
            
        return output
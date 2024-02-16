class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        num = ""
        while i < len(s) and s[i] == " ":
            i+= 1
        if i >= len(s):
            return 0
        sign = 1
        if s[i] == "-":
            sign = -1
            i+=1
        elif s[i]== "+":
            i+=1
        while(i < len(s) and s[i].isdigit()):
            num+=s[i]
            i+=1
        if len(num) == 0:
            return 0
        num = int(num)*sign
        
        if num < -(2**31):
            num = -(2**31)
        elif num > 2**31-1:
            num = 2**31-1
        return num

        
            
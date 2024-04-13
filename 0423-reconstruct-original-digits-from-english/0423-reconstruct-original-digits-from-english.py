class Solution:
    def originalDigits(self, s: str) -> str:
        d = {}
        digits = [0]*10
        for char in s:
            if char in d:
                d[char]+=1
            else:
                d[char]=1
        while "z" in d:
            for char in "zero":
                d[char]-=1
                if d[char] == 0:
                    del d[char]
            digits[0]+=1

        while "w" in d:
            for char in "two":
                d[char]-=1
                if d[char] == 0:
                    del d[char]
            digits[2]+=1
        while "u" in d:
            for char in "four":
                d[char]-=1
                if d[char] == 0:
                    del d[char]
            digits[4]+=1
        while "x" in d:
            for char in "six":
                d[char]-=1
                if d[char] == 0:
                    del d[char]
            digits[6]+=1
        while "g" in d:
            for char in "eight":
                d[char]-=1
                if d[char] == 0:
                    del d[char]
            digits[8]+=1
        while "o" in d:
            for char in "one":
                d[char]-=1
                if d[char] == 0:
                    del d[char]
            digits[1]+=1
        while "s" in d:
            for char in "seven":
                d[char]-=1
                if d[char] == 0:
                    del d[char]
            digits[7]+=1
        while "g" in d:
            for char in "eight":
                d[char]-=1
                if d[char] == 0:
                    del d[char]
            digits[8]+=1
        while "h" in d:
            for char in "three":
                d[char]-=1
                if d[char] == 0:
                    del d[char]
            digits[3]+=1
        while "f" in d:
            for char in "five":
                d[char]-=1
                if d[char] == 0:
                    del d[char]
            digits[5]+=1
        while "n" in d:
            for char in "nine":
                d[char]-=1
                if d[char] == 0:
                    del d[char]
            digits[9]+=1
        output = ""
        print(digits)
        for i in range(10):
            for _ in range(digits[i]):
                output += str(i)
        return output
         


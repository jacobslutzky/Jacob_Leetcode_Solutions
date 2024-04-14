class Solution:
    def findLatestTime(self, s: str) -> str:
        new_string = ""
        if s[0] == "?" and s[1] == "?":
            new_string += "11"
        elif s[0] == "?":
            if s[1] == "1" or s[1] == "0":
                new_string += "1" + s[1]
            else:
                new_string += "0" + s[1]
        elif s[1] == "?":
            if s[0] == "1":
                new_string += "11"
            else:
                new_string += "09"
        else:
            new_string+= s[:2]
        
        new_string += ":"

        if s[3] == "?":
            new_string += "5"
        else:
            new_string += s[3]
        if s[4] == "?":
            new_string += "9"
        else:
            new_string += s[4]
        
        return new_string
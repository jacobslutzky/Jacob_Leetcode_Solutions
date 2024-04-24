class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}

        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        for char in t:
            if char not in d:
                return False
            else:
                d[char] -= 1
                if d[char] == 0:
                    del d[char]
        return not d
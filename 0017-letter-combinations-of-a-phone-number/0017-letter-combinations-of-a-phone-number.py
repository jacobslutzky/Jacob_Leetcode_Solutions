class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        output = []
        def get_combinations(digits, curr):
            if not digits:
                if curr:
                    output.append(curr)
                return
            
            for char in d[digits[0]]:
                get_combinations(digits[1:], curr + char)
            
        get_combinations(digits, "")
        return output
        

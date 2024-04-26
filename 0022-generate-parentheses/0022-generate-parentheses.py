class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def recurse(i, stack, output):
            if len(output) >= n*2:
                results.append(output)

                return
            
            print(stack)
            print(output)
            print()
            
            if i < n:
                recurse(i+1, stack + ["("], output + "(")
            if stack:
                recurse(i, stack[:-1], output + ")")
        
            

        recurse(0, [], "")
        return results
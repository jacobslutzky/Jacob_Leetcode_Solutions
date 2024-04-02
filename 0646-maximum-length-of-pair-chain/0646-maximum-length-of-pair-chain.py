class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x : x[1])
        print(pairs)
        max_chain = 1
        start = 0
       
        for i in range(1, len(pairs)):
            if pairs[i][0] > pairs[start][1]:
                
                max_chain += 1
                start=i
        return max_chain
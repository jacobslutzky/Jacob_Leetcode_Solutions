class Solution:
    def compress(self, chars: List[str]) -> int:    
        i = 1
        count = 1
        curr_stream = 1
        while i < len(chars):
            count+=1
            if chars[i] == chars[i-1]:
                while i < len(chars) and chars[i] == chars[i-1]:
                    curr_stream+=1
                    chars.pop(i)
                for num in str(curr_stream):
                    chars.insert(i,num)
                    i+=1
                    count+=1
                
            curr_stream = 1
            i+=1
        return count
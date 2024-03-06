class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_list = [{} for _ in range(17)]
        for word in words:
            words_list[len(word)][word] = 1
        
        max_count = 1
        for length in range(2,17):
            for word in words_list[length]:
                    for i in range(length):
                        curr_word = word[:i] + word[i+1:]
                        if curr_word in words_list[length-1]:      
                            words_list[length][word] = max(words_list[length-1][curr_word]+1,words_list[length][word])
                            max_count = max(max_count,words_list[length][word] )
                        
        return max_count


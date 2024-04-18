class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_lists = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagram_lists:
                anagram_lists[sorted_word].append(word)
            else:
                anagram_lists[sorted_word] = [word]
        output = []
        for key in anagram_lists:
            output.append(anagram_lists[key])
        
        return output


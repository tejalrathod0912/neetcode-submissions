class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for word in strs:
            new_word = "".join(sorted(word))

            if new_word not in dic:
                dic[new_word] = [word]
            else:
                new_word_list = dic[new_word]
                dic[new_word].append(word)

        return list(dic.values())
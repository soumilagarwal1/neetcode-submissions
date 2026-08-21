class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordmap = {}
        for word in strs:
            if ''.join(sorted(word)) not in wordmap:
                wordmap[''.join(sorted(word))] = [word]
            else:
                wordmap[''.join(sorted(word))].append(word)
        return list(wordmap.values())



        
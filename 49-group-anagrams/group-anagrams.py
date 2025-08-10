class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        for word in strs:
            key = ''.join(sorted(word))
            anagrams.setdefault(key, []).append(word)
        return list(anagrams.values())

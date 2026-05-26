class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            sorted_i = ''.join(sorted(i))
            if sorted_i not in hashmap:
                hashmap[sorted_i] = []
            hashmap[sorted_i].append(i)
        return list(hashmap.values())
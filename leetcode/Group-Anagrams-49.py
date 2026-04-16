from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = defaultdict(list)
        res = []
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c)-ord("a")] += 1
            key = tuple(count)
            mem[key].append(word)
        
        return list(mem.values())

# TC : O(N*M)
# SC : O(N*M)

# sorting method
# TC : O(N*K*logK)

# Suggested: Hash Table/Sorting/Array
# Key Idea: Group anagrams by using sorted strings as hash keys to identify equivalent character compositions.
# Consider: Could you optimize the sorting step by using character frequency counts instead?

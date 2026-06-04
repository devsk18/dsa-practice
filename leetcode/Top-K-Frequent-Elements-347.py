from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)

        bucket = [0] * (n+1)

        for num, freq in counter.items():
            if bucket[freq] == 0:
                bucket[freq] = [num]
            else:
                bucket[freq].append(num)
        
        res = []
        for i in range(n, -1, -1):
            if bucket[i] != 0:
                res.extend(bucket[i])
            if len(res) == k:
                break
        
        return res

# TC: O(n)
# SC: O(n)

# Suggested: Hash Table/Counting/Bucket Sort
# Key Idea: Using frequency buckets to achieve linear time complexity for finding top k frequent elements.
# Consider: Since you nailed the O(n) approach, how would you adapt this if the input stream was infinite?

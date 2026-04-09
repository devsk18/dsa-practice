class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(intervals)
        intervals.sort(key=lambda x:x[0])

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1] = [res[-1][0], max(res[-1][1], interval[1])]
        return res

# TC = O(N log N)
# SC = O(N)

# Suggested: Sorting/Greedy
# Key Idea: Sort intervals by start time then greedily merge overlapping ranges in a single pass.

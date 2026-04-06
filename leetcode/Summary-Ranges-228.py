class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        res = []
        cur_start = nums[0]

        for i in range(len(nums)):
            if i != 0:
                prev = nums[i-1]
                if nums[i]-1 != prev:
                    if cur_start == prev:
                        res.append(str(cur_start))
                    else:
                        res.append(str(cur_start) + "->" + str(prev))
                    cur_start = prev = nums[i]
        
        if cur_start == nums[-1]:
            res.append(str(cur_start))
        else:
            res.append(str(cur_start) + "->" + str(nums[-1]))
        
        return res

# TC: O(N)
# SC: O(N)

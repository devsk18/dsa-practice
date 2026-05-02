class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxA = -1 * math.inf
        l, r = 0, n-1

        while l < r:
            # calculate area - use min(2 heights) and diff btw them
            # if H of l < r then l ++ else r --

            area = min(height[l], height[r]) * abs(l-r)
            maxA = max(maxA, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxA

# TC : O(N)
# SC = O(1)

# Suggested: Two Pointers/Greedy
# Key Idea: Using two pointers moving inward from ends, always advancing the shorter line to maximize potential area.
# Consider: Can you prove why moving the taller pointer inward would never yield a larger area than the current one? - by keeping taller one, we increase the chance to find a better height than the previous short line to generate better area

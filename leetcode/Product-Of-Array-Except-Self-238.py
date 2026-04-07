class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = 1
        res = [0] * n

        for i in range(n):
            res[i] = prod
            prod *= nums[i]
        
        prod = 1
        for i in range(n-1, -1, -1):
            res[i] *= prod
            prod *= nums[i]

        return res

# TC = O(N)
# SC = O(1)

# Suggested: Prefix Sum/Array
# Key Idea: Calculating prefix and suffix products to determine the product of all elements except self without division.

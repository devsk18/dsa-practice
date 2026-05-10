class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, (m*n)-1

        while lo <= hi:
            mid = lo + ((hi-lo)//2)
            r, c = mid//n, mid%n
            val = matrix[r][c]
            if val == target:
                return True
            elif val > target:
                hi = mid-1
            else:
                lo = mid+1
            
        return False

# TC : O(log M*N)
# SC : O(1)

# Suggested: Binary Search/Array
# Key Idea: Treating a 2D sorted matrix as a flattened 1D sorted array to apply binary search.

class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        sum = 0
        prev = 0

        for i in s:
            sum += map[i]
            if prev!=0 and map[prev] < map[i]:
                sum -= map[prev]*2 # we added it once so subtract twice
            prev = i

        return sum

# TC : O(N)
# SC : O(1)

# Suggested: Array/Simulation
# Key Idea: Iterate through the string while comparing adjacent values to handle subtraction cases.
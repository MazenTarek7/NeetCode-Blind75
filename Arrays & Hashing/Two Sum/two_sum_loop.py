"""
Time Complexity: O(n^2) - Due to nested loops iterating through the array.
Space Complexity: O(1).
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ansArr = []
        for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ansArr.append(i)
                    ansArr.append(j)
        return ansArr

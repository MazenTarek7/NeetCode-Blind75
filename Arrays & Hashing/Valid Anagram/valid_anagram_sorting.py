"""
Time Complexity: O(n log n)
Space Complexity: O(n).
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

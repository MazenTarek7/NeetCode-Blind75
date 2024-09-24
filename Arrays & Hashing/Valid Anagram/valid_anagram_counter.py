"""
Time Complexity: O(n)
Space Complexity: O(1) - The space complexity is O(1) because the number of unique characters is bounded by the size of the character set.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t) or len(t) > len(s):
            return False
        count_S = Counter(s)
        count_T = Counter(t)
        if count_S == count_T:
            return True
        return False

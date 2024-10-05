class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = Counter(sorted(nums)).most_common()
        res = []
        for i in range(0, k):
            res.append(ans[i][0])
        return res
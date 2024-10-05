class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[]]

        if len(strs) == 1:
            return [[strs[0]]]

        ansArr = [[] for i in range(len(strs))]
        original_strs = strs.copy()
        strs = [''.join(sorted(x)) for x in strs]
        ansArr[0].append(original_strs[0])
        for i in range(1, len(strs)):
            added = False
            for j in range(i):
                if ansArr[j] and strs[j] == strs[i]:
                    ansArr[j].append(original_strs[i])
                    added = True
                    break
            if not added:
                ansArr[i].append(original_strs[i])
        return [group for group in ansArr if group]
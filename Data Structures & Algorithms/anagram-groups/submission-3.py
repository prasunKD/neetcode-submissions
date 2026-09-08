class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''l1 = []
        l2 = []
        l3 = []
        for k in strs:
            a = list(k)
            a.sort()
            l3.append(a)
        length = len(strs)
        seen = [False] * length
        for i in range(length):
            if seen[i]: 
                continue
            l2.append(strs[i])
            seen[i] = True
            for j in range(i+1, length):
                if not seen[j] and l3[i] == l3[j]:
                    l2.append(strs[j])
                    seen[j] = True
            l1.append(l2)
            l2 = []
        return l1'''

        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

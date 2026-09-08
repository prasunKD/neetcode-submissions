class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # b = []
        # k = 0
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[]

        D = {}
        for num in nums:
            if num in D:
                D[num] += 1
            else:
                D[num] = 1
            
            
        A = [[D[k],k] for k in D.keys()]
        A = sorted(A, reverse=True)
        
        ans = []
        for i in range(k):
            ans.append(A[i][1])
        
        return ans

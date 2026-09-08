class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = 0
        #l2 = nums
        l = len(nums)
        '''for i in range(l):
            val = l2.pop(0)
            if val in l2:
                return True
                a = 1
                break
            l2.append(val)
        if a == 0:
            return False'''
        nums.sort()
        for i in range(l-1):
            if nums[i] == nums[i+1]:
                a=1
                return True
                break
        
        if a == 0:
            return False

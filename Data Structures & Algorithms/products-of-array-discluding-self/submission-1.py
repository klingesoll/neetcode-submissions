class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [0] * n #创造一个长度为n的列表，里面每个位置先放0
        #因为在 Python 里，列表可以用乘法重复自己。即为把列表 [0] 重复 n 次

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                 continue
                prod *= nums[j]
            
            res[i] = prod
        return res
        


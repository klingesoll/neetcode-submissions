# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:

#         n = len(nums)
#         res = [0] * n #创造一个长度为n的列表，里面每个位置先放0
#         #因为在 Python 里，列表可以用乘法重复自己。即为把列表 [0] 重复 n 次

#         for i in range(n):
#             prod = 1
#             for j in range(n):
#                 if i == j:
#                  continue
#                 prod *= nums[j]
            
#             res[i] = prod
#         return res
        

class Solution: #optimal
      def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums) - 1, -1, -1): #range(start,stop,step)
           res[i] *= postfix
           postfix *= nums[i]

        return res
# 暴力法是对每个位置重新遍历数组，跳过自己，时间 O(n²)。

# 优化思路是：每个位置的答案等于左边乘积乘右边乘积。

# 所以我可以先构造 pref 数组，pref[i] 表示 i 左边所有元素的乘积；
# 再构造 suff 数组，suff[i] 表示 i 右边所有元素的乘积；
# 最后 res[i] = pref[i] * suff[i]。

# 这样时间复杂度是 O(n)，空间复杂度是 O(n)。

# 进一步可以省掉 pref 和 suff：
# 先用 res 存左边乘积，再从右往左用 postfix 变量滚动维护右边乘积。
# 最终做到 O(n) 时间，O(1) 额外空间。


from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [1] * n
        right = [1] * n
        res = [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(n):
            res[i] = left[i] * right[i]

        return res
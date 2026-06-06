class Solution:
    def maxArea(self, heights: List[int]) -> int:
         res = 0

         for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                area = min(heights[i],heights[j]) * (j - i)
                res = max(res, area)
         return res
         
#         暴力：枚举所有左右边界，O(n²)
# 优化：从最大宽度开始，双指针向内收缩
# 原则：谁短移动谁
# 原因：短板决定水位，移动长板没用
# 复杂度：O(n)
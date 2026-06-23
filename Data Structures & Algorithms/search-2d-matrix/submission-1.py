from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows * cols - 1

        while l <= r:
            mid = l + (r - l) // 2

            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
        
        # 1.每次都检查每行最后一个数字，如果大于目标值的话就在这行找就行了，小于目标值就跳到下一行最后一个值
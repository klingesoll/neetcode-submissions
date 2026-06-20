class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indices = {} #字典
# ```python
# indices = {
#     2: 0,
#     7: 1,
#     11: 2,
#     15: 3
# }
# ```

        for i, n in enumerate(nums):
            indices[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n 

            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j > i + 1 and nums[j] == nums[j - 1]: #如果当前 j 不是第一个可选的第二个数，并且当前数字和前一个数字一样，那就跳过它。
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])
            
            for j in range(i + 1 ,len(nums)): #当前这个 i 的内层循环结束了，把刚才被 j 临时拿走的数字全部还回 count。
                count[nums[j]] += 1
        return res
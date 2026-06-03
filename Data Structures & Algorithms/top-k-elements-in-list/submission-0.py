class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1+ count.get(num, 0) #计数的常用方法

        arr = []
        for num,cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1]) #9:32 PMClaude responded: k 是题目传进来的参数，意思是"返回前 k 个最频繁的元素"。k 是题目传进来的参数，意思是"返回前 k 个最频繁的元素"。
        return res










# 1. 统计每个数出现几次：用count.get(num, 0) + 12. 
# 2.找次数最多的前k个：创造一个计数的数组，以数出现的次数为键，将对应的数映射到键上？




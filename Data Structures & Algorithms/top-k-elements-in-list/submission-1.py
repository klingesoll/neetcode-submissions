# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         for num in nums:
#             count[num] = 1+ count.get(num, 0) #计数的常用方法

#         arr = []
#         for num,cnt in count.items():
#             arr.append([cnt, num])
#         arr.sort()

#         res = []
#         while len(res) < k:
#             res.append(arr.pop()[1]) #9:32 PMClaude responded: k 是题目传进来的参数，意思是"返回前 k 个最频繁的元素"。k 是题目传进来的参数，意思是"返回前 k 个最频繁的元素"。
#         return res










# 1. 统计每个数出现几次：用count.get(num, 0) + 12. 
# 2.找次数最多的前k个：创造一个计数的数组，以数出现的次数为键，将对应的数映射到键上？



class Solution:
    def topKFrequent(self, nums, k):
        #1. 统计次数
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        #2. 建桶(即空列表）， index = 出现次数
        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)


        #3.从后往前取k个
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        # range(起点, 终点, 步长)
        # 终点永远不包含
        


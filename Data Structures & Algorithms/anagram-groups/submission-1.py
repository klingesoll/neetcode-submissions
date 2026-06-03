# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
#         for s in strs:
#             sortedS = ''.join(sorted(s))#sorted是把字符串拆成字符按字母顺序排列，返回的是列表，''.join(...) — 把列表里的字符拼回字符串，
#                         # 中间用 '' 连接（即没有分隔符）
#             res[sortedS].append(s)
#         return list(res.values())

# #         res = {
# #     "aet": ["eat", "tea", "ate"],
# #     "ant": ["tan", "nat"],
# #     "abt": ["bat"]
# # }



#         # defaultdict(list) — 访问不存在的 key 自动创建空列表



class Solution(object):
    def groupAnagrams(self, strs):
        res = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in res:
                res[key] = []
            res[key].append(s)
        return list(res.values())
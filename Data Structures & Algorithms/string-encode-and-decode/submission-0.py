class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) #因为 s[0:1] 切出来是字符串 "3"，不是数字 3，要用 int() 转换才能做加法 i + length。
            i = j + 1
            j = i + length
            res.append(s[i:j]) #因为处理完一段之后，i 要移到下一段的起点：
            i = j

        return res


class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = '' #空字符串用来保存有效字符
        for c in s:
            if c.isalnum(): #is alphabet or number
                newStr += c.lower()
        return newStr == newStr[::-1] 
         #把字符串反过来 字符串[start : end : step]
         #从 start 开始，到 end 结束，按照 step 的步长取字符
        
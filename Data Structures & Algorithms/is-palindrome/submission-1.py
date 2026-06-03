class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1 #多变量赋值等价于l = 0 r = len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

        # 1.准备两个指针 l r
        # 2.l如指向无效字符就向右移动，同理，r向左移动
        # 3.如果两边都是有效字符就比较，直到指针相遇
        # 4.不相同就return False

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

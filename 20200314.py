# no.7 整数反转
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            y = int(str(abs(x))[::-1])
        elif x < 0:
            y = 0 - int(str(abs(x))[::-1])
        if y < -2 ** 31 or y > 2 ** 31:
            y = 0
        return y

# 没想到字符转换速度反而慢了。尝试数学直接计算
    def reverse_cacu(self, x: int) -> int:
        y, res = abs(x), 0
        out_limit = 2 ** 31 -1 if x > 0 else 2 ** 31
        while y != 0:
            res = res * 10 + y % 10
            if res > out_limit:
                res = 0
            y //= 10
        return res if x > 0 else -res

# example = Solution().reverse(-123)
# example = Solution().reverse_cacu(-543)
# print(example)

# no.9 回文数

class Solution:
    # 全返
    def isPalindrome(self, x: int) -> bool:
        if x > 0:
            y, res = x, 0
            while y != 0:
                res = res * 10 + y % 10
                y //= 10
            return True if res == x else False
        elif x <= 0:
            return True if x == 0 else False

    # 半反
    def isPalindrome_half(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x % 10 == 0:
            return False
        else:
            res = 0
            while x > res:
                res = res * 10 + x % 10
                x //= 10
            if x == res or res // 10 == x:
                return True
            else:
                return False

example = Solution()
print(example.isPalindrome_half(0))
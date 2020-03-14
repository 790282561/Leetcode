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
example = Solution().reverse_cacu(-543)
print(example)

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

# 没想到字符转换速度反而慢了。明天研究一下数学解法

example = Solution().reverse(-123)
print(example)

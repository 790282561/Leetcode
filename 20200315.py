# no.13罗马数字转整数
class Solution:
    # 分离4或9
    def romanToInt(self, s: str) -> int:
        dict1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        j = 0
        for i in s:
            j += dict1.get(i)
        print(j)
        if 'IV' in s or 'IX' in s:
            j -= 2
        if 'XL' in s or 'XC' in s:
            j -= 20
        if 'CD' in s or 'CM' in s:
            j -= 200
        return j

    # 官方思路
    def romanToInt_2(self, s: str) -> int:
        dict1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int = 0
        for index in range(len(s) - 1):
            if dict1.get(s[index]) < dict1.get(s[index + 1]):
                int -= dict1.get(s[index])
            else:
                int += dict1.get(s[index])
        return int + dict1.get(s[-1])


example = Solution()
print(example.romanToInt_2("MCMXCIV"))

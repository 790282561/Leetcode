# no.14最长公共前缀
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ''
        i = 0
        ls_final = ''
        strs = sorted(strs, key=lambda x:len(x))
        print(strs)
        while i < len(strs[0]):
            ls = set()
            for str in strs:
                ls.add(str[i])
            print(ls)
            if len(ls) == 1:
                ls_final += ls.pop()
                i += 1
                print(i)
            return ls_final

example = Solution()
print(example.longestCommonPrefix(["flower","flow","flight"]))
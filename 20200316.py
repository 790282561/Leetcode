# no.14最长公共前缀
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ''
        i = 0
        ls_final = ''
        strs = sorted(strs, key=lambda x:len(x))
        for i in range(len(strs[0])):
            ls = set()
            for str in strs:
                ls.add(str[i])
            if len(ls) == 1:
                ls_final += ls.pop()
            elif len(ls) != 1:
                break
        return ls_final

    def longestCommonPrefix_Zip(self, strs) -> str:
        ls = list(zip(*strs))
        ls_final = ''
        for i in ls:
            if len(set(i)) == 1:
                ls_final += i[0]
            else:
                break
        return ls_final

example = Solution()
print(example.longestCommonPrefix_Zip(["dog", 'abg']))
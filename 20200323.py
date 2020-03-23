# no.20有效的括号
class Solution:
    # 利用栈的思路
    def isValid(self, s: str) -> bool:
        test_var = []
        tag = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in tag.values():
                test_var.append(i)
            elif i in tag.keys():
                if len(test_var) == 0:
                    test_var.append(i)
                elif test_var[-1] != tag[i]:
                    test_var.append(i)
                elif test_var[-1] == tag[i]:
                    test_var.pop()
                else:
                    test_var.append(i)
            else:
                pass
        return True if len(test_var) == 0 else False

    # 正序括号和倒序括号的顺序相同则为真
    # 该方法有问题，'()[]{}'报错，但是'{[()]}'正确
    def isValid_2(self, s: str) -> bool:
        left, right = [], []
        tag = {')': '(', ']': '[', '}': '{'}
        s = s.replace(' ', '')
        if len(s) == 0:
            return True
        elif s[-1] in tag.values():
            return False
        else:
            for i in s:
                if i in tag.keys():
                    right.append(tag[i])
                else:
                    left.append(i)
        return left == list(reversed(right))

    # 同样栈方法，用"?"解决空字符串问题
    def isValid_3(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1


def main():
    s = "([)]"
    example = Solution()
    print(example.isValid(s))


if __name__ == '__main__':
    main()

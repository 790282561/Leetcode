a = 1


def foo(a):
    def foo2():
        b = a + 2
        return b

    return foo2


c = foo(a)()  # 无论如何要调用两次，所以这里可以用return foo2()或foo(a)()两种方式完成
print(c)


def foo(a):
    def foo2():
        b = a + 2
        return b

    return foo2()


d = foo(a)  # 无论如何要调用两次，所以这里可以用return foo2()或foo(a)()两种方式完成
print(d)

# def multiplier(factor):
#     def multiplyByFactor(number):
#           return number*factor
#     return multiplyByFactor
#
# c = multiplier(2)(5)
# print(c)

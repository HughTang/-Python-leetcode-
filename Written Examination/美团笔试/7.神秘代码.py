'''
测试用例：
输入：
6 1
hhhaaa
输出：
hahaha
'''
# 加密
def encryption(s):
    ans = ''
    while len(s) > 0:
        # 向上取整并落实到s的下标
        mid = (len(s) + 1) // 2 - 1
        ans += s.pop(mid)
    return ans

# 解密
def decode(s):
    ans = []
    for i in range(1,len(s)+1):
        mid = (i + 1) // 2 - 1
        ans.insert(mid, s.pop())
    return ''.join(ans)


if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    s = list(input())
    # 加密
    if m == 1:
        print(encryption(s))
    # 解密
    else:
        print(decode(s))
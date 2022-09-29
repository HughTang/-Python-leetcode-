# 
# [编程之美3.1] 字符串循环移位
# 
# 问题：将字符串向右循环移动 k 位。
# 算法思想：将 abcd123 中的 abcd 和 123 单独翻转，得到 dcba321，然后对整个字符串进行翻转，得到 123abcd。
# 
def reverseString1(s: str, k: int) -> str:
    # 注意使用s[::-1]时，规则与s[::]是一样的，只不过s[::-1]是逆序
    # 同样地，逆序时的起始下标可以遍历到，而结束下标需要-1才可以；顺序时结束下标需要+1才可以。
    s1 = s[len(s)-k-1::-1]  # dcba
    s2 = s[-1:len(s)-k-1:-1] # 321
    s = s1 + s2
    return s[::-1]

# 方法二
def reverseString2(s: str, k: int) -> str:
	n = len(s)
    k %= n
	return s[n-k:] + s[:n-k]

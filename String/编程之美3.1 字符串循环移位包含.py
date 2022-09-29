# 
# [编程之美3.1] 字符串循环移位包含
# 
# 问题：给定两个字符串 s1 和 s2，要求判定 s2 是否能够被 s1 做循环移位得到的字符串包含。
# 算法思想：s1 进行循环移位的结果是 s1s1 的子字符串，因此只要判断 s2 是否是 s1s1 的子字符串即可。
# 
def isContainsByConcat(s1: str, s2: str) -> bool:
    if not s1 or not s2:
        return False
    s1 = s1*2
    if s1.find(s2):
        return True
    return False
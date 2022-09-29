#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#

# @lc code=start
class Solution:
    # 分治算法：
    # 该问题的子问题就是 x op y 中的 x 和 y：以运算符分隔的左右两侧算式解，而且只有当x或y为数字的时候，才能进行直接求解。
    # 然后我们来进行分治算法三步走：
    # （1）分解：按运算符分成左右两部分，分别求解
    # （2）解决：实现一个递归函数，输入算式，返回算式解
    # （3）合并：根据运算符合并左右两部分的解，得出最终解

    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 如果只有数字，则直接返回，注意返回的是列表，因为后面的left和right需要遍历
        if expression.isdigit():
            return [int(expression)]

        res = list()
        for i,c in enumerate(expression):
            if c in ('+', '-', '*'):
                # 1.分解：遇到运算符，计算左右两侧的结果集
                # 2.解决：diffWaysToCompute 递归函数求出子问题的解
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                # 3.合并：根据运算符合并子问题的解
                for l in left:
                    for r in right:
                        if c == '+':
                            res.append(l+r)
                        elif c == '-':
                            res.append(l-r)
                        else:
                            res.append(l*r)
        return res
# @lc code=end


#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
class Solution:
    # 算法思路：
    # （1）通过将列表中的每个元素进行异或运算，得到只出现一次的两个数（比如分别为x，y）的异或值diff，
    # 然后利用diff &= -diff得出diff最右侧为1的位，同时其他位置置0，由于diff中1的位是x和y在该位置异或
    # 得到的，所以x和y在该位上是不同的，一个是0，一个是1。
    # （2）利用两数在该位不同的特征，通过逐个判断nums中的元素在该位的数值，将nums的元素分为两部分，然后
    # 每个部分的元素都进行异或操作，就得到了两部分只出现一次的元素（即「136.只出现一次的数字」中的思路）。
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 将nums中所有元素进行异或操作获得两个目标数值的异或值
        diff = functools.reduce(lambda x,y: x^y, nums)
        # 保留diff中最右边的1，其他位置0
        diff &= -diff
        # a和b分别初始化为0（初始化为0的原因：a^0=a）
        a, b = 0, 0
        # 对于nums中的每个元素，按照其与diff的与操作，将元素分别归为两部分，最后的结果存储在a和b中
        for v in nums:
            # 元素v与diff中的1位置相同
            if v & diff:
                a ^= v
            # 元素v与diff中的1位置不同
            else:
                b ^= v
        # 返回最后结果
        return [a,b]

# @lc code=end


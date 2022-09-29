#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start
class Solution:
    # 本题的思路不难，但是考验算法的优化方法，从而有效避免算法超时。
    # 本题的优化方法在于用一个字典同时存储给定数组的数值及相应数值
    # 所在的下标和个数，如下格式：{数值1：[下标1，下标2，...，下标m]}
    # 即{数值：下标列表}的方法来存储，这样既可以获取某数值的范围，
    # 也可以通过len()的方法获取特定数值在数组中出现的次数，一举两得。
    # 最后只需要一个min()函数配合字典的values()遍历即可获得最终结果。
    def findShortestSubArray(self, nums: List[int]) -> int:
        # 初始化字典，其中按照{数值：下标列表}的方式存储
        dic = dict()
        for i,v in enumerate(nums):
            # 如果v已经在字典中，将其下标i加入到v所对应的下标列表中
            if v in dic:
                dic[v].append(i)
            # 如果v不在字典中，将v及其下标列表进行存储，注意这里的[i]将其初始化为一个下标列表
            else:
                dic[v] = [i]
        # 获取数组的度
        degree = max(len(i) for i in dic.values())
        # 返回最短连续子数组
        return min(i[-1] - i[0] for i in dic.values() if len(i) == degree) + 1 
# @lc code=end


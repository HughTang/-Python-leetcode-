#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    '''
        本题的思路是构建递减栈，即栈里只有递减元素。
        （1）遍历整个数组，如果栈不空，且当前数字大于栈顶元素，
    那么如果直接入栈的话就不是递减栈 ，所以需要取出栈顶元素，由
    于当前数字大于栈顶元素的数字，而且一定是第一个大于栈顶元素的
    数，直接求出下标差就是二者的距离。
        （2）继续看新的栈顶元素，直到当前数字小于等于栈顶元素停止，
    然后将数字入栈，这样就可以一直保持递减栈，且每个数字和第一个大
    于它的数的距离也可以算出来。
        该方法的时间复杂度为O(n)，空间复杂度为O(n)。
    '''
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 初始化结果列表为len(T)个0，防止出现ans下标溢出的情况，
        # 同时能够将没有递增元素的位置初始化为0
        ans = [0]*len(T)
        # 初始化stack用于存放T中递减温度的下标值
        stack = list()
        # 遍历T的下标
        for i in range(len(T)):
            # 当栈不为空且当前下标所指示温度大于栈顶下标所指示温度时循环
            while stack and T[i] > T[stack[-1]]:
                # 弹出栈顶下标
                index = stack.pop()
                # 将栈顶下标的结果赋值为 当前下标-栈顶下标
                ans[index] = i - index
            # 循环条件不成立时，将当前下标进栈
            stack.append(i)
        # 返回结果列表
        return ans
    
    # 更容易编码和理解的方法二：使用enumerate(T)同时将T中的[i,v]存储到stack中，方便后续比较和处理
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0]*len(T)
        stack = list()
        for i, v in enumerate(T):
            while stack and v > stack[-1][1]:
                k = stack.pop()[0]
                ans[k] = i - k
            stack.append([i,v])
        return ans 

# @lc code=end


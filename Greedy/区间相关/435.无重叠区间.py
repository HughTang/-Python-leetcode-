#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    # 算法思想：
    # 在每次选择中，区间的结尾最为重要，选择的区间结尾越小，留给
    # 后面的区间的空间越大，那么后面能够选择的区间个数也就越大。
    # 因此需要按区间的结尾进行排序，每次选择结尾最小，并且和前一
    # 个区间重叠的区间。
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 按照每个区间的结尾进行排序
        takesecond = lambda elem : elem[1]
        intervals.sort(key = takesecond)
        
        # prev表示前一个区间的结尾元素，初始化为负无穷
        # float("-inf")表示负无穷（注：float("inf")表示正无穷）
        prev = float("-inf")
        # ans表示需要移除区间的个数，初始化为0
        ans = 0
        
        # 对每个区间进行遍历
        for ls in intervals:
            # 如果当前区间的起始元素>=前一个区间的结尾元素，表示区间无重叠，则prev变成当前区间的结尾元素
            if ls[0] >= prev:
                prev = ls[1]
            # 如果当前区间的起始元素<前一个区间的结尾元素，表示区间重叠，ans++
            else:
                ans += 1
        
        # 返回最终结果
        return ans
    
    # 第二次刷题记录：本题目与算法课视频中的例子思想相同，该题目的贪心策略只能从以下三个方面考虑：
    # （1）开始位置：从开始位置考虑的话，会出现移除区间不是最小数量的问题，因为虽然开始位置足够小，但可能其所占的区间过大，导致移除的区间数量过多。
    # （2）间隔距离：从每个区间的间隔距离考虑，间隔距离越小，并不代表其重复区间的数量就越少，因此不可以作为贪心准则。
    # （3）结束位置：从结束位置考虑，对结束位置进行递增排序，选择的区间结束位置越小，留给后面的区间去选择余地越大，从而保证删除重叠区间的数量最少。
    # 因此，此处选用结束位置作为贪心策略的准则，以找到需要移除重叠区间的最小数量。
    # 第二次刷题时所编写的代码，与第一次官方解答的区别主要在于pre值的选择，以及for循环是值循环还是下标循环，基本思想是一致的，只是一些细节不同。
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        takesecond = lambda elem: elem[1]
        intervals.sort(key=takesecond)
        pre_num = intervals[0][1]
        ans = 0
        for i in range(1,len(intervals)):
            if pre_num > intervals[i][0]:
                ans += 1
            else:
                pre_num = intervals[i][1]
        return ans
# @lc code=end


#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    # 贪心算法：以区间结尾为贪心策略即可。
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        takesecond = lambda elem: elem[1]
        points.sort(key=takesecond)
        # 由于题目中说明points的长度最小为1，因此不存在为空的情况，所以ans初始化为1，以保证最后一个气球区间能够引爆
        ans = 1
        end = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] > end:
                ans += 1
                end = points[i][1]
        return ans
    
    # 第二次刷题解法，区别不大
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        ans = 0
        end = float('-inf')
        for point in points:
            if point[0] > end:
                ans += 1
                end = point[1]
        return ans
# @lc code=end


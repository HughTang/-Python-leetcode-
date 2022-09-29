#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    # 根据二分查找的万能式，该问题要找的是蓝色区域最右边的值（蓝色在左，红色在右）
    def mySqrt(self, x: int) -> int:
        # l和r初始化为蓝色区域的边界-1，红色边界+1
        l, r = -1, x+1
        while l + 1 < r:
            mid = l + (r-l) // 2
            # 蓝色区域的判断条件为mid*mid <= x
            if mid * mid <= x:
                l = mid
            else:
                r = mid
        # 由于最终的结果是要向下取整，所以需要返回l
        return l
# @lc code=end


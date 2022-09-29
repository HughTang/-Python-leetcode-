#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start


class Solution:
    # 方法一：数学
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            visited.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
            if n in visited:
                break
        return n == 1
    
    # 方法二：双指针
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = sum([int(i) ** 2 for i in str(slow)])
            fast = sum([int(i) ** 2 for i in str(fast)])
            fast = sum([int(i) ** 2 for i in str(fast)])
            if slow == fast:
                break
        return slow == 1
# @lc code=end

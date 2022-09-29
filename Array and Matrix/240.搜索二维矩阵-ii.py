#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    # 本题根据给定矩阵的性质，将行和列的下标初始化为左下角的元素下标
    # 然后根据元素值与target的大小向上或向右移动，直到找到target或者
    # 下标超出范围。
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        # 行
        row = len(matrix)-1
        # 列
        col = 0
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        return False
# @lc code=end


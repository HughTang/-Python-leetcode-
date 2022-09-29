#
# @lc app=leetcode.cn id=766 lang=python3
#
# [766] 托普利茨矩阵
#

# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # 获取行长和列长
        row, col = len(matrix), len(matrix[0])
        # 遍历所有元素下标，如该元素的值与右下角的元素值不相等，
        # 则返回False，要注意对下标溢出的情况进行判断。
        # 在上述情况下，易知矩阵最后一行的元素是无需判断的，因此
        # 外层循环的条件可以将row改为row-1，从而提高效率。
        for i in range(row-1):
            for j in range(col-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        # 若所有元素满足条件，则返回True
        return True

# @lc code=end


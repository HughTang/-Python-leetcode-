#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第 K 小的元素
#

# @lc code=start
class Solution:
    # 二分查找的万能式，充分利用排序矩阵的性质，从左下角元素开始：
    # （1）若当前元素<=mid，记录元素个数，向右移动；
    # （2）若当前元素>mid，向上移动；
    # 通过上述方法即可找到mid在矩阵中的边界，结果的左半部分都是
    # <=mid的元素，而右半部分都是>mid的元素。最后根据左半部分的
    # 元素个数与k比较来改变left或right的值，然后循环直到left+1>right
    # 才终止。
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0]-1, matrix[-1][-1]+1
        while left + 1 < right:
            mid = (left + right) // 2
            num = 0
            
            # 二分查找
            i, j = n - 1, 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            
            # right指示右边的红色部分
            if num >= k:
                right = mid
            # left指示左边的蓝色部分
            else:
                left = mid
        return right
# @lc code=end


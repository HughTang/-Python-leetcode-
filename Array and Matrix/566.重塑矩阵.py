#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    # 本题的思路很简单，遍历所有元素，c个元素为一组截取即可。
    # 注：在本题的解题过程中，遇到了python内存机制相关的问题，
    # 由于每次sub_list都需要加入到new_mat中去，而受python引用
    # 机制的影响，new_mat中加入的其实是sub_list所指向对象的引用，
    # 当时用sub_list.clear()时会将sub_list所引用对象清空，导致
    # 之前已经加入到new_mat中的sub_list发生改变，从而导致结果错误，
    # 所以在这里只能使用sub_list = [] 的置空方法，才能保证其原来
    # sub_list所指向的列表内存空间不变。
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # 如果没有办法转化，直接返回原矩阵
        if len(mat)*len(mat[0]) != r*c:
            return mat
        # 要返回的矩阵
        new_mat = list()
        # 当前行
        sub_list = list()
        for words in mat:
            for word in words:
                # 当前元素入行
                sub_list.append(word)
                # c个元素成一行
                if len(sub_list) == c:
                    new_mat.append(sub_list)
                    # 下一行置空，继续遍历
                    sub_list = []
                    # 请特别注意，下面这一行的置空操作在本题中是不可行的
                    # sub_list.clear()
        # 返回新矩阵
        return new_mat


# @lc code=end


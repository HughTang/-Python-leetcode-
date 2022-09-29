#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    # 算法思路：
    # 只需要将flowerbed前后各加一个0就可以避免分情况讨论，直接遍历寻找三个相邻的0即可
    #
    # 写法一：写法比写法二更简洁
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0
    
    # 写法二：由于可以提前返回，因此用时比写法一少，效率更高
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False
# @lc code=end


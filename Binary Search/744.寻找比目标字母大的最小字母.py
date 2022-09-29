#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#

# @lc code=start
class Solution:
    # 寻找红色区域的最左侧元素
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = -1, len(letters)
        while l + 1 < r:
            mid = l + (r - l) // 2
            if letters[mid] <= target:
                l = mid
            else:
                r = mid
        return letters[r] if r < len(letters) else letters[0]
# @lc code=end


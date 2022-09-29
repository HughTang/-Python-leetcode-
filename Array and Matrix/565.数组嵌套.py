#
# @lc app=leetcode.cn id=565 lang=python3
#
# [565] 数组嵌套
#

# @lc code=start
class Solution:
    # 本题为了避免超时，是不允许暴力求解的，由于在每次计算
    # 嵌套数组长度结束之后，再次访问该数组的已访问元素时，
    # 得到的长度与之前是一致的，因此属于冗余计算，只需要把
    # 之前访问过的元素进行标记即可节省计算时间。
    # 
    # 方法一：不使用额外空间。直接将原数组访问过的元素改为-1，
    # 当再次访问时对元素值是否为-1进行判断，从而实现上述过程。
    # 该题解的时间复杂度为O(N)，空间复杂度为O(1)。
    def arrayNesting(self, nums: List[int]) -> int:
        # 初始化结果长度
        length = 0
        for i in range(len(nums)):
            # cnt用于记录每次循环的结果长度
            cnt = 0
            index = i
            while nums[index] != -1:
                cnt += 1
                t = nums[index]
                nums[index] = -1
                index = t
            length = max(length,cnt)
        return length
    
    # 方法二：使用额外空间，将已经访问过的元素下标在visited集合中记录
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        ans = 0
        for i,v in enumerate(nums):
            cnt = 0
            while i not in visited:
                visited.add(i)
                cnt += 1
                i = nums[i] 
            ans = max(ans,cnt)
        return ans
# @lc code=end


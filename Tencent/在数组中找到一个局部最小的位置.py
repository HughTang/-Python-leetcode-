# 题目要求：
# 定义局部最小的概念。arr长度为1时，arr[0]是局部最小。arr的长度为N(N>1)时，如果arr[0]<arr[1]，
# 那么arr[0]是局部最小；如果arr[N-1]<arr[N-2]，那么arr[N-1]是局部最小；
# 如果0<i<N-1，既有arr[i]<arr[i-1]，又有arr[i]<arr[i+1]，那么arr[i]是局部最小。
# 
# 给定无序数组arr，已知arr中任意两个相邻的数不相等。写一个函数，只需返回arr中任意一个局部最小出现的位置即可
# 
# [要求]
# 时间复杂度为O(\log n)O(logn)，空间复杂度为O(1)O(1)

# 链接：https://www.nowcoder.com/questionTerminal/d1c8838fc9e54b89bc10b5b6d2b52157

# 二分查找
class Solution:
    def local_min_index(self, nums):
        if len(nums) <= 1:
            return -1
        if nums[0] < nums[1]:
            return 0
        if nums[-1] < nums[-2]:
            return len(nums)-1
        low, high = 1, len(nums)-2
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid-1] < nums[mid]:
                high = mid
            elif nums[mid+1] < nums[mid]:
                low = mid
            else:
                return mid
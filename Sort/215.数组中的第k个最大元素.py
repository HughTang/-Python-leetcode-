#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
#
# 该题是排序算法的经典题目，除了会做这道题外，还会重点对排序的细节思路进行注释讲解。
class Solution:
    # 方法一：暴力解法
    #     升序排序以后，目标元素的索引是len - k。这是最简单的思路，如果只答这个方法，面试官可能并不会满意，但是在我们平时的开发工作中，还是不能
    # 忽视这种思路简单的方法，理由如下：
    # （1）最简单同时也一定是最容易编码的，编码成功的几率最高，可以用这个最简单思路编码的结果和其它思路编码的结果进行比对，验证高级算法的正确性；
    # （2）在数据规模小、对时间复杂度、空间复杂度要求不高的时候，简单问题简单做；
    # （3）简单的算法思路，有些时候可以为实现高级算法铺路，这道题也是如此；
    # （4）低级算法往往容错性最好，即在输入不满足题目条件的时候，往往还能得到正确的答案，而高级算法对输入数据的要求就非常苛刻，这一点可以参考
    # 「4. 寻找两个有序数组的中位数」。
    #     时间复杂度：O(NlogN)，空间复杂度：O(1)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]
    
    
    # 方法二：快速排序1
    # 使用自定义的快速排序方法来代替方法一中的sort()函数，该方法是为了熟悉快速排序的思想，但是效率不及系统的sort()方法。
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quick_sort(nums, 0, len(nums)-1)
        return nums[len(nums)-k]
    
    def quick_sort(self, nums: List[int], low: int, high: int):
        if low < high:
            pivotpos = self.partition(nums, low, high)
            self.quick_sort(nums, low, pivotpos - 1)
            self.quick_sort(nums, pivotpos + 1, high)
    
    def partition(self, nums: List[int], low: int, high: int) -> int:
        pivot = nums[low]
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= pivot:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivot
        return low

    # 方法三：快速排序2
    # 结合该题目的要求，设计适合该题解思路的快速排序方法，由于每趟快速排序都能确定一个元素在排序后数组的最终位置，因此可以在
    # 某趟排序时直接将符合条件的元素返回。
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low, high = 0, len(nums) - 1
        target = len(nums) - k
        while True:
            pivotpos = self.partition(nums, low, high)
            if pivotpos == target:
                return nums[pivotpos]
            elif pivotpos < target:
                low = pivotpos + 1
            else:
                high = pivotpos - 1


    def partition(self, nums: List[int], low: int, high: int) -> int:
        pivot = nums[low]
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= pivot:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivot
        return low

    # 方法四：堆排序（优先队列）
    # 使用容量为 k 的小顶堆
    # 元素个数小于 k 的时候，放进去就是了
    # 元素个数大于 k 的时候，小于等于堆顶元素，就扔掉，大于堆顶元素，就替换
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for i in range(k):
            # heapq 默认就是小顶堆
            heapq.heappush(heap, nums[i])
        for i in range(k, len(nums)):
            if heap[0] < nums[i]:
                # 若当前元素比堆顶元素大，则替换堆顶元素
                heapq.heapreplace(heap, nums[i])
        # 最后堆顶中的元素就是堆中最小的，整个数组中的第 k 大元素
        return heap[0]

    # 方法五：堆排序2
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return min(heapq.nlargest(k,nums))

# @lc code=end
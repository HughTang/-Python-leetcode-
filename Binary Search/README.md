## 二分查找（Binary Search）

### 1、二分查找两大原则
- 每次都要缩减搜索区域
- 每次缩减不能排除潜在答案

### 2、三大模板
#### （1）找一个准确值
- 循环条件：l <= r
- 缩减搜索空间：l = mid + 1, r = mid - 1
#### （2）找一个模糊值（例如：比4大的最小数）
- 循环条件：l < r
- 缩减搜索空间：l = mid, r = mid - 1 或者 l = mid + 1, r = mid
#### （3）万用型（完全适配前两个模板的使用条件）
- 循环条件：l + 1 < r
- 缩减搜索空间：l = mid, r = mid

### 3、万用型的解释
![avator](https://note.youdao.com/yws/public/resource/92524f6bde32729673febedf95825926/xmlnote/D72F33583B77439593DF592F651B7CBD/41159)
![avator](https://note.youdao.com/yws/public/resource/92524f6bde32729673febedf95825926/xmlnote/F7CA61BEF6C44EF7B3165271CD003574/41161)
![avator](https://note.youdao.com/yws/public/resource/92524f6bde32729673febedf95825926/xmlnote/70E9B5959DA349D28C5A6968F30AAB92/41165)
![avator](https://note.youdao.com/yws/public/resource/92524f6bde32729673febedf95825926/xmlnote/91ED6AD403014547B0E2B231D5736688/41163)
![avator](https://note.youdao.com/yws/public/resource/92524f6bde32729673febedf95825926/xmlnote/B1CCB1F4FA6B4859B405E41F84A50261/41167)
![avator](https://note.youdao.com/yws/public/resource/92524f6bde32729673febedf95825926/xmlnote/C8B5476D516046C6828023931352A68B/41169)
![avator](https://note.youdao.com/yws/public/resource/92524f6bde32729673febedf95825926/xmlnote/F3E1EFCAA8FD4243872D6B5B69D91200/41171)
![avator](https://note.youdao.com/yws/public/resource/92524f6bde32729673febedf95825926/xmlnote/8CC9E41FFFAC42EB973BFA5640D8CEE6/41173)
![avator](https://note.youdao.com/yws/public/resource/92524f6bde32729673febedf95825926/xmlnote/BB29A6FB28BF4972AEC69A1A9855C0ED/41175)

### 4、万用型编码方式
##### 以「704.二分查找」为例，代码如下。
```python
class Solution:
    # 方法一：传统方法（模板1的方式）
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1
    
    # 方法二：万能式（蓝色区域最右侧的值）
    def search(self, nums: List[int], target: int) -> int:
        l, r = -1, len(nums)
        while l + 1 < r:
            mid = l + (r-l) // 2
            # 将nums[mid]==target的情况置于蓝色区域的最右侧值
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        # 判断target是否查找成功
        return l if nums[l] == target else -1

    # 方法三：万能式（红色区域最左侧的值）
    def search(self, nums: List[int], target: int) -> int:
        l, r = -1, len(nums)
        while l + 1 < r:
            mid = l + (r-l) // 2
            # 将nums[mid]==target的情况置于红色区域的最左侧值
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        # 判断r是否越界，以及target是否查找成功
        return r if r < len(nums) and nums[r] == target else -1
```
> 参考视频网址：https://www.bilibili.com/video/BV1d54y1q7k7?from=search&seid=4909399090510315831&spm_id_from=333.337.0.0

### 5、题目分类
##### 万用型
- 69.sqrt(x)
- 278.第一个错误的版本
- 704.二分查找
- 744.寻找比目标字母大的最小字母
- 34.在排序数组中查找元素的第一个和最后一个位置
##### 其他
- 153.寻找旋转排序数组中的最小值
- 540.有序数组中的单一元素 
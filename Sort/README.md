## 排序基础知识
### 1、Python的堆操作
#### Python中的heap主要通过heapq中的API来实现，以下为heapq中的常用API。

```python
    # 导入heapq包
    import heapq
    # 将x压入堆中
    heapq.heappush(heap, x)   
    # 从堆中弹出最小的元素                                     
    heapq.heappop(heap)    
    # 让列表具备堆特征                                  
    heapq.heapify(heap) 
    # 弹出最小的元素，并将x压入堆中                                      
    heapq.heapreplace(heap, x)  
    # 返回iter中n个最大的元素                          
    heapq.nlargest(n, iter) 
    # 返回iter中n个最小的元素                                      
    heapq.nsmallest(n, iter)                                   
    # 从一个list中获取最大的元素
    max_column_data = heapq.nlargest(1, temp_list, key=lambda item: len(item))
```

---
### 2、Python中自带的sort()函数原理
#### （1）简单介绍
##### `sort()`函数中所采用的排序方法是`Timsort`方法，该方法结合了`合并排序（merge sort）`和`插入排序（insertion sort）`而得出的排序算法，它在现实中有很好的效率。Tim Peters在2002年设计了该算法并在Python中使用（TimSort 是 Python 中` list.sort `的默认实现）。该算法找到数据中已经排好序的块-分区，每一个分区叫一个`run`，然后按规则合并这些run。Pyhton自从2.3版以来一直采用Timsort算法排序，现在Java SE7和Android也采用Timsort算法对数组排序。

#### （2）Timsort核心过程
##### TimSort 算法为了减少对升序部分的回溯和对降序部分的性能倒退，将输入按其升序和降序特点进行了分区。排序的输入的单位不是一个个单独的数字，而是一个个的块-分区。其中每一个分区叫一个 run。针对这些run序列，每次拿一个run出来按规则进行合并。每次合并会将两个run合并成一个 run。合并的结果保存到栈中。合并直到消耗掉所有的 run，这时将栈上剩余的 run合并到只剩一个 run 为止。这时这个仅剩的 run 便是排好序的结果。

### （3）相关操作
##### 现实中的大多数据通常是有部分已经排好序的，Timsort利用了这一特点。Timsort排序的输入的单位不是一个个单独的数字，而是一个个的分区。其中每一个分区叫一个“run“。针对这个 run 序列，每次拿一个 run 出来进行归并。每次归并会将两个 run 合并成一个 run。每个run最少要有2个元素。Timesort按照升序和降序划分出各个run：run如果是是升序的，那么run中的后一元素要大于或等于前一元素；如果run是严格降序的，即run中的前一元素大于后一元素，需要将run中的元素翻转（这里注意降序的部分必须是“严格”降序才能进行翻转。因为 TimSort 的一个重要目标是保持稳定性stability。如果在 >= 的情况下进行翻转这个算法就不再稳定。

### （4）性能分析
##### Timsort是稳定的算法，当待排序的数组中已经有排序好的数，它的时间复杂度会小于`nlogn`。与其他合并排序一样，Timesrot是稳定的排序算法，最坏时间复杂度是`O（nlogn）`。在最坏情况下，Timsort算法需要的临时空间是`n/2`，在最好情况下，它只需要一个很小的临时存储空间。

### （5）不采用快速排序的原因
##### 大多数语言的内置排序API函数不使用快速排序的原因由于快速排序的不稳定性。

###### 参考博客：https://www.cnblogs.com/clement-jiao/p/9243066.html


---
### 3、Python中的sort()函数使用
#### sort()方法语法：
```python
    list.sort(cmp=None, key=None, reverse=False)
```
#### 参数：
- cmp -- 可选参数, 如果指定该参数会使用该参数的方法进行排序。
- key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序，一般传入的是一个定义好的函数。
- reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
#### 返回值：
- 该方法没有返回值，但是会对列表的对象进行排序。
#### 举例：
「435. 无重叠区间」中按照嵌套子列表的第二个元素进行升序排列：
```python
    takesecond = lambda x : x[1]
    intervals.sort(key = takesecond)  # 其中intervals为[[1,2], [2,3], [3,4], [1,3]]的格式
```

---
### 3、Python中的sorted()函数使用
#### sorted()方法语法：
```python
    sorted(iterable, cmp=None, key=None, reverse=False)
```
#### 参数：
- iterable -- 可迭代对象。
- cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
- key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
- reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
#### 返回值：
- 返回重新排序的列表。
#### *sort 与 sorted 区别：*
- sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
- list 的 sort 方法对列表原地排序，无返回值；内建函数 sorted 方法返回的是一个新的 list，原列表不会发生变化。


---
### 5、相关排序算法思想

### 插入排序

#### （1）直接插入排序（Straight Insertion Sort）
##### 算法思想
- 每次都将当前元素插入到左侧已经排序的数组中，使得插入之后左侧数组依然有序。
##### 时间复杂度：
- 平均情况：O(N²)
- 最好情况：O(N)，数组已经有序
- 最坏情况：O(N²)，数组逆序
##### 空间复杂度：
- O(1)
##### 稳定性：
- 稳定

#### （2）折半插入排序（Binary Insertion Sort）
##### 算法思想
- 折半插入排序是对直接插入排序算法的一种改进，由于前半部分为已排好序的数列，这样我们不用按顺序依次寻找插入点，可以采用折半查找的方法来加快寻找插入点的速度。
##### 时间复杂度：
折半插入排序算法比直接插入算法明显**减少了关键字之间比较的次数**，因此速度比直接插入排序算法快，**但记录移动的次数没有变**，所以折半插入排序算法的时间复杂度仍然为O(N²)，与直接插入排序算法相同。
- 平均情况：O(N²)
- 最好情况：O(N)，数组已经有序
- 最坏情况：O(N²)，数组逆序
##### 空间复杂度：
- O(1)
##### 稳定性：
- 稳定

#### （3）希尔排序（Shell's Sort）
##### 算法思想
- 希尔排序又称为“缩小增量排序”，是直接插入排序算法的一种更高效的改进版本。希尔排序是把序列按下标的一定增量分组，对每组元素使用直接插入排序算法排序；随着增量逐渐减少，每组包含的元素越来越多，当增量减至 1 时，所有元素都被分成一组，算法便终止。
##### 时间复杂度：
- 平均情况：O(![avatar](https://bkimg.cdn.bcebos.com/formula/eb39d4c67a9cabbd3a2690a2151ee6cc.svg))
##### 空间复杂度：
- O(1)
##### 稳定性：
- 不稳定

### 交换排序

#### （4）冒泡排序（Bubble Sort）
##### 算法思想
- 从左到右不断交换相邻逆序的元素，在一轮的循环之后，可以让未排序的最大元素上浮到右侧。在一轮循环中，如果没有发生交换，那么说明数组已经是有序的，此时可以直接退出。
##### 时间复杂度：
- 平均情况：O(N²)
- 最好情况：O(N)，数组已经有序
- 最坏情况：O(N²)，数组逆序
##### 空间复杂度：
- O(1)
##### 稳定性：
- 稳定

#### （5）快速排序（Quicksort）
##### 算法思想
- 通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
##### 时间复杂度：
- 平均情况：O(Nlog₂N)
- 最好情况：O(Nlog₂N)，基准元素选取得当，每次都能均匀的划分序列
- 最坏情况：O(N²)，基准元素恰好是最大或最小元素
##### 空间复杂度：
- O(log₂N)，递归树的深度
##### 稳定性：
- 不稳定
##### 实现源码：
```python
    # 快速排序递归实现
    def quick_sort(self, nums: List[int], low: int, high: int):
        if low < high:
            pivotpos = self.partition(nums, low, high)
            self.quick_sort(nums, low, pivotpos - 1)
            self.quick_sort(nums, pivotpos + 1, high)
    
    # pivot的优化选取：随机选取
    def partition(self, nums: List[int], low: int, high: int) -> int:
        pos = random.randint(low, high)
        # 将low与pos的元素交换位置，此时可以和普通的快排一样执行划分函数
        nums[low], nums[pos] = nums[pos], nums[low]

        # 普通快排的划分步骤
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
```
> 快排优化思路：https://blog.csdn.net/insistGoGo/article/details/7785038

### 选择排序

#### （6）简单选择排序（Select Sort）
##### 算法思想
- 从数组中选择最小元素，将它与数组的第一个元素交换位置。再从数组剩下的元素中选择出最小的元素，将它与数组的第二个元素交换位置。不断进行这样的操作，直到将整个数组排序。
##### 时间复杂度：
- 平均情况：O(N²)
- 最好情况：O(N²)
- 最坏情况：O(N²)
##### 空间复杂度：
- O(1)
##### 稳定性：
- 不稳定

#### （7）堆排序（Heapsort）
##### 算法思想
- 堆排序是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。堆排序可以说是一种利用堆的概念来排序的选择排序。
##### 时间复杂度：
- 平均情况：O(Nlog₂N)
- 最好情况：O(Nlog₂N)
- 最坏情况：O(Nlog₂N)
##### 空间复杂度：
- O(1)
##### 稳定性：
- 不稳定

### 归并排序

#### （8）二路归并排序
##### 算法思想
- 把待排序序列分为若干个子序列，每个子序列是有序的，然后再把有序子序列合并为整体有序序列。归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法的一个非常典型的应用。 
##### 时间复杂度：
- 平均情况：O(Nlog₂N)
- 最好情况：O(Nlog₂N)
- 最坏情况：O(Nlog₂N)
##### 空间复杂度：
- O(N)
##### 稳定性：
- 稳定




##### 附图：各种排序算法的复杂度和稳定性
![avatar](https://note.youdao.com/yws/public/resource/92524f6bde32729673febedf95825926/xmlnote/D735962EFA0940978BF15279D36C1821/33170)

##### Tips：快速选择和堆排序都可以求解 `Kth Element` 和 `TopK Elements` 问题。

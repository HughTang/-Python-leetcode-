## 动态规划

### 1、算法特征
#### （1）同质子结构
#### （2）最优子结构
#### （3）存在重叠子问题
#### （4）无后效性：当前的决策不受未来决策的影响
#### （5）逆向组解

### 2、动态规划的设计要点
#### （1）同质子结构
#### （2）状态转移方程
#### （3）备忘录（全局变量）

### 3、动态规划的实现方法
#### （1）顺推：从已知状态的子问题逐步推出复杂问题的解，一般用循环实现。例如已知f(1)和f(2)，可以推出f(3)。
#### ![avatar](https://note.youdao.com/yws/public/resource/92524f6bde32729673febedf95825926/xmlnote/8B94325B37CA4656A578C86B59F548F2/36681)

#### （2）递归：将目标问题一步步拆分为子问题，直到找到可以直接求解的子问题，然后逐级反馈。例如要求f(20)，需要先求出f(19)和f(18)。
#### ![avatar](https://note.youdao.com/yws/public/resource/92524f6bde32729673febedf95825926/xmlnote/47E7AA7F138C4A06A8BB6587E0A749D3/36683)
#### ![avatar](https://note.youdao.com/yws/public/resource/92524f6bde32729673febedf95825926/xmlnote/FBC23F7237AF4A3F919DB8F138F334BE/36685)

### 4、背包问题
#### 以下图片中的f(w,i)中的w表示背包剩余重量，i表示物品剩余种类数量。
#### （1）0-1背包问题的现实描述
![avatar](https://note.youdao.com/yws/public/resource/372ddacb31c50d8d76d6ae783350696d/xmlnote/09E3941853C24E55A735B65ADD212A5C/38261)
#### （2）0-1背包问题的数学描述
![avatar](https://note.youdao.com/yws/public/resource/372ddacb31c50d8d76d6ae783350696d/xmlnote/E30A6B4F4D864C58BFBC49B48664CCAA/38263)
#### （3）0-1背包问题的状态转移方程
![avatar](https://note.youdao.com/yws/public/resource/372ddacb31c50d8d76d6ae783350696d/xmlnote/3768F1FFA10A4D79A143B71200799E9B/38265)
#### （4）完全背包
![avatar](https://note.youdao.com/yws/public/resource/372ddacb31c50d8d76d6ae783350696d/xmlnote/CC3FACFFAF8540A5BE05A72E2B6E4D27/38268)
#### （4）多重背包
![avatar](https://note.youdao.com/yws/public/resource/372ddacb31c50d8d76d6ae783350696d/xmlnote/211A37BE439047C9AFC53ABE7B2099D4/38271)
#### （5）分组背包
![avatar](https://note.youdao.com/yws/public/resource/372ddacb31c50d8d76d6ae783350696d/xmlnote/BA95D2ADE36741B8A07BBFB59BA1EC23/38273)

#### 注：[0-1背包问题的二维转一维思路讲解](https://mp.weixin.qq.com/s/xmgK7SrTnFIM3Owpk-emmg)、[背包问题讲解汇总](https://leetcode-cn.com/problems/target-sum/solution/gong-shui-san-xie-yi-ti-si-jie-dfs-ji-yi-et5b/)

### 5、股票交易
#### 股票交易本质上属于多状态（2~4个状态）的动态规划问题，基本状态主要是以下两种状态：
- have数组: 手上持有股票的最大收益，第一个元素需要初始化为-prices[0]，因为如果第0天就持有股票，则其一定是买了prices[0]
- no数组: 手上不持有股票的最大收益
#### 参考网址：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/si-wei-dao-tu-zheng-li-gu-piao-wen-ti-da-9jir/

### 6、最长公共子序列与字符串编辑（二维DP）
#### （1）问题定义：给定两个字符串或者数组，求解以下问题：
- 两个字符串的最长公共子序列的长度（1143.最长公共子序列）
- 两个字符串的最长公共子序列（1143.最长公共子序列的变体）
- 利用最少的删除操作使得两个字符串相同（583.两个字符串的删除操作）
- 利用最少的替换、删除、插入操作将str1转化为str2（72.编辑距离）
#### （2）DP方法
- 建立二维dp[i][j]，情况一：表示 str1[0:i-1] 和 str2[0:j-1] 的最长公共子序列；情况二：表示将 str1[0:i-1] 转换为 str2[0:j-1] 的最少操作数。
#### （3）DP状态说明
- text1[0:i-1] 表示的是 text1 的 第 0 个元素到第 i - 1 个元素，两端都包含，之所以 dp[i][j]的定义不是 text1[0:i] 和 text2[0:j] ，是为了方便当 i = 0 或者 j = 0 的时候，dp[i][j]表示的为空字符串和另外一个字符串的匹配，这样 dp[i][j]可以初始化为 0
#### （4）状态转移方程：
- ①当 text1[i - 1] == text2[j - 1] 时，说明两个子字符串的最后一位相等，所以最长公共子序列又增加了 1，所以 dp[i][j]与dp[i - 1][j - 1]相关。
- ②当 text1[i - 1] != text2[j - 1] 时，说明两个子字符串的最后一位不相等，那么此时的状态 dp[i][j] 应该与 dp[i - 1][j] 和 dp[i][j - 1]有关，如果是含有替换操作，则dp[i][j]还与dp[i-1][j-1]有关

### 7、贪心算法与动态规划的比较
#### 相同点：
- 处理的问题都具有 同质子结构、最优子结构、无后效性 的特征。
#### 不同点：
- 贪心算法的优点是解法效率高，思路简单；缺点是没办法对所有问题实现最优解。
- 动态规划的优点是所得的结果一定是全局最优解；缺点是只适用于能够总结出状态转移方程的问题，且效率比贪心算法低。

### 8、做题记录
#### （1）关于dp初始化与dp下标
- 若dp中的 **下标 不参与 状态转移方程** 的计算过程，则**dp初始化为n个**即可，**dp[0]可以代表实际问题为1**的情况，后面的**for循环中结束为n**（斐波那契数列、矩阵路径、数组区间）

- 若dp中的**下标 参与了 状态转移方程** 的计算过程，**dp需要初始化为n+1个**，且dp[0]一般无意义或者临界，**dp[1]代表代表实际问题为1**的情况，后面的**for循环中也要注意改为n+1**（分割整数）

#### （2）关于0-1背包问题中优化空间后遍历方式的改变
- 由于0-1背包问题的状态转移方程为dp[i][w] = max(dp[i-1][w], dp[i-1][w-wi] + ci)，其中dp[i][w]的原始意义为还剩i个物品的情况下填满容量为w的背包所能带走的最大价值，而大部分0-1背包题目中的i表示第i个状态，且其代表的**状态dp[i][w]取决于且仅取决于上一个状态dp[i-1][w]和dp[i-1][w-wi]的取值**，因此如果要优化空间，**将dp从二维数组转化为一维数组求解时**，必须保证dp的每轮循环赋值使用的都是前一个状态（**前一个物品的外层循环固定，对内层背包容量循环后得到的dp值**）的值，因此只需要进行**逆序遍历**，就能**保证第i个状态的dp每次赋值的是第i-1个状态的赋值结果**。
- 参考网址1：https://mp.weixin.qq.com/s/xmgK7SrTnFIM3Owpk-emmg
- 参考网址2：https://blog.csdn.net/mch2869253130/article/details/81906962
- 参考网址3：https://blog.csdn.net/u010982765/article/details/79044613

#### （3）关于完全背包问题中优化空间后仍采取正序遍历方式的解释
![avator](https://note.youdao.com/yws/public/resource/92524f6bde32729673febedf95825926/xmlnote/F133578F256B4C768711EA07DBB9C10E/39396)

视频网址：https://www.bilibili.com/video/BV15v411y7Qz/?spm_id_from=trigger_reload

#### （4）0-1背包与完全背包的优化对比
![avator](https://note.youdao.com/yws/public/resource/92524f6bde32729673febedf95825926/xmlnote/01D989F79F6047A3B7C832277E900DFC/39398)
#### （5）关于背包问题的编码思路
```python
    1.处理特定背包问题的边界/特殊情况
    2.初始化dp列表，一般是以下面的形式初始化
    dp=[0] + [X] * W
    3.for循环的嵌套，外层循环一般为物品列表的遍历，内层循环一般为dp下标范围/问题结果范围，0-1背包的内层循环为逆序，完全背包的内层循环为正序。
    4.注意：如果求解的是关于顺序的完全背包问题时，对物品的迭代应该放在最里层，对背包的迭代放在外层，只有这样才能让物品按一定顺序放入背包中。（139.单词拆分）（377.组合总和-iv）
    for v in nums:
        # 无论是0-1背包还是完全背包，下面的内层循环中都通过修改range中的范围来省略“背包容量<物品容量”的情况
        # 0-1背包
        for i in range(w,v-1,-1):
        # 完全背包
        for i in range(v,w+1):
            # 一般形式举例，其中的+1为物品价值为1的特殊情况，若规定了不同物品的不同价值，+1应该替换为具体的价值+C[v]
            # （1）最大个数、最长序列、最大价值
            dp[i] = max(dp[i],dp[i-v]+1)
            # （2）最小个数、最短序列、最小价值
            dp[i] = min(dp[i],dp[i-v]+1)
            # （3）不同的方案总数
            dp[i] += dp[i-v]
            # （4）是否存在某方案
            dp[i] = dp[i] or dp[i-v]
    4.返回最终结果
    return dp[-1]
```
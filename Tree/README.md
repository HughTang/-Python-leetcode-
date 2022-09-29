### 树
#### 1、遍历
##### （1）前序遍历：栈，根先进栈，然后根节点的右孩子进栈，左孩子进栈，进栈时需要判断非空。
```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        ans = list()
        while stack:
            node = stack.pop()
            ans.append(node.val)
            # 先右后左，保证出栈时先遍历左子树
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans
```
##### （2）中序遍历：栈，当前节点cur，先利用cur找到最左侧节点，然后出栈node，cur指向node.right，循环条件为cur or stack，cur进栈不需要判断非空。
```python
class Solution:
    # 中序遍历为left -> root -> right
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = list()
        ans = list()
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            ans.append(node.val)
            cur = node.right
        return ans
```
##### （3）后序遍历：栈，利用前序遍历的思路，只是要先左孩子进栈，然后右孩子进栈，进栈时需要判断非空，最后返回结果列表的倒序。
```python
class Solution:
    # 前序遍历为root->left->right，后序遍历为left->right->root。
    # 可以修改前序遍历成为 root -> right -> left，那么这个顺序就
    # 和后序遍历正好相反。
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        ans = list()
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans[::-1]
```
##### （4）层序遍历：队列，先将根节点入队，然后获取队列的长度，将当前长度的所有节点依次出队，并将其左孩子与右孩子节点入队，进队时需要判断非空。
```python
class Solution:
    # 经典层次遍历问题，需要借助队列进行遍历节点的存取，
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # 定义队列，用于存取节点
        queue = [root]
        # ans用于存放
        ans = list()
        # 队列判空循环
        while queue:
            # 获取当前队列的长度
            length = len(queue)
            # 当前队列中节点的循环处理
            for _ in range(length):
                # 出队赋值给node
                node = queue.pop()
                # num的加法处理
                ans.append(node.val)
                # 判断出队节点的左子树是否为空，不为空则入队
                if node.left:
                    queue.insert(0, node.left)
                # 判断出队节点的右子树是否为空，不为空则入队
                if node.right:
                    queue.insert(0, node.right)
        # 返回结果列表
        return ans
```
#### 2、递归
#### （1）二叉树的深度、直径及平衡二叉树的判断
##### 该类题目一般需要借助「104.二叉树的最大深度」的max_depth()函数的基本框架，如果是求直径或者其他该类型题目的变体，一般还需要提前定义并初始化self.result变量，在max_depth()的递归过程中实时更新self.result的值。
```python
class Solution:
    '''
    如果我们知道了左子树和右子树的最大深度l和r，那么该二叉树的
    最大深度即为max(l,r)+1,而左子树和右子树的最大深度又可以以
    同样的方式进行计算。因此我们可以用「深度优先搜索」的方法来
    计算二叉树的最大深度。具体而言，在计算当前二叉树的最大深度
    时，可以先递归计算出其左子树和右子树的最大深度，然后在O(1)
    时间内计算出当前二叉树的最大深度。递归在访问到空节点时退出。
    该方法的时间复杂度为O(N)，空间复杂度为O(height)。
    '''
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        r = self.maxDepth(root.right)
        l = self.maxDepth(root.left)
        return max(r,l) + 1
``` 
##### 典型题目如下：
- 104.二叉树的最大深度（max_depth直接应用）
- 111.二叉树的最小深度（max_depth中间加入l与r为0的判断）
- 110.平衡二叉树（self.result、max_depth中间加入abs(l-r)>1的平衡因子判断）
- 543.二叉树的直径（self.result、max_depth每次递归获取所处根节点的最大左右子树的深度值之和）
- 687.最长同值路径（思路拓展，self.result、left_path与right_path）

#### （2）二叉树路径判断
##### 一般用于不确定匹配的初始节点位置，需要对每个节点作为初始匹配节点的情况进行判断，比如从上到下的寻找节点值之和等于target的路径数目，或者在一棵树中匹配另一个树的子树。
##### 该类题目求解一般需要两个函数f1和f2，一般在f1中以f2(root)+f1(root.left)+f1(root.right)的形式（+号根据题目不同可能会改为or、and等连接符或计算符）进行f1与f2的递归调用。
##### 典型题目如下：
- 437.路径总和-iii
- 572.另一个树的子树

#### （3）一般性质递归
##### 本类题目没有固定求解思路，只能根据相关题意，结合树的性质进行合理递归设计。
##### 典型题目如下：
- 101.对称二叉树
- 112.路径总和
- 226.翻转二叉树
- 337.打家劫舍-iii
- 404.左叶子之和
- 617.合并二叉树
- 671.二叉树中第二小的节点
- 剑指Offer 34.二叉树中和为某一值的路径
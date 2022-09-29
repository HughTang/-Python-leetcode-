### ACM模式下的注意事项
#### 1、对于需要同时判断多条数据是否符合题意条件的情况，逐个读入数据进行处理时的解决方案如下：
```python
# 单个数据条目的判断函数
def judge(*args, **klwargs):
    pass

if __name__ == '__main__':
    # n为需要判断的独立数据条目数量
    n = int(input())
    # data存储所有的数据
    data = []
    # 逐个读入并放入data中
    for _ in range(n):
        data.append(input())
    # 对data中的每个数据调用judge函数进行独立判断
    for x in data:
        print(judge(x))
```
##### 代表题目：
- 七星不靠（网易互娱）
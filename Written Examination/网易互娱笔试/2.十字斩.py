def jugde(matrix):
    # 获取每列的元素和
    col_sum = [sum(col) for col in list(zip(*matrix))]
    y = col_sum.index(max(col_sum))
    for row in matrix:
        row.pop(y)

    # 获取除去y这一列后的每行的元素和
    row_sum = [sum(row) for row in matrix]
    x = row_sum.index(max(row_sum))
    matrix.pop(x)

    return x+1,y+1

if __name__ == '__main__':
    n = int(input())
    matrix = []
    # 输入字符串后的转数字处理过程
    for _ in range(n):
        ls = []
        for c in input().split():
            ls.append(int(c))
        matrix.append(ls)
    # 调用判断函数
    for _ in range(n):
        x, y = jugde(matrix)
        print(str(x)+' '+str(y))

    
'''
题目描述：第一行输入的n表示要点击几次，后面8行字符串为消消乐的8*8矩阵的红蓝绿方格的排布，再后面8行为消除后要填补的字符串，
然后后面的n行是每次点击操作的坐标（1~8）和方块填补方向（w表示向上落，s表示向下落，a表示向左落，d表示向右落），其中纵向的操作
需要按列填充，横向的操作需要按行填充，求每次消除操作后消除的方格数量。
'''

'''
测试用例如下:
2
rbbbrrrb
ggggbrbr
rrrggbrr
gbrgbrrr
bgbgrrrg
bgbgbrrb
rggrgggg
bgbrgrgr
bbrgggggbbgbbbrg
bbgbrgbgbbgbbbrg
brgbgbbggbbgbbbr
gbbgbbbrggrbbgrb
bgrbbrgggrbrgbrr
brgbrgbrgrgbrgbr
brbbrbbbrbrrggrg
ggrbrgbgbrgggrbr
1 5 w
1 4 d
'''

def dfs(matrix, row, col, target) -> int:
        global ans, directions
        if row < 0 or row >= 8 or col < 0 or col >= 8 or matrix[row][col] == '0' or matrix[row][col] != target:
            return 0  
        matrix[row][col] = '0'
        ans += 1
        # 针对四个方向进行DFS递归遍历
        for i,j in directions:
            dfs(matrix, row+i, col+j, target)

def change_a():
    global matrix,nexts
    for i,s in enumerate(nexts):
        n = matrix[i].count('0')
        for _ in range(n):
            matrix[i].remove('0')
            matrix[i].append(s.pop(0))

def change_d():
    global matrix,nexts
    for i,s in enumerate(nexts):
        n = matrix[i].count('0')
        for _ in range(n):
            matrix[i].remove('0')
            matrix[i].insert(0,s.pop(0))


def change_w():
    global matrix,nexts
    ls = []
    for i in range(8):
        n = 0
        for j in range(8):
            if matrix[j][i] == '0':
                n += 1
                if j+1 < 8:
                    matrix[j][i] = matrix[j+1][i]
                    matrix[j+1][i] = '0' 
        ls.append(n)
    for i,v in enumerate(ls):
        for k in range(8-v,8):
            matrix[k].pop(i)
            matrix[k].insert(i,nexts[i].pop(0))

def change_s():
    global matrix,nexts
    ls = []
    for i in range(8):
        n = 0
        for j in range(8):
            if matrix[j][i] == '0':
                n += 1
                if j-1 >= 0:
                    matrix[j][i] = matrix[j-1][i]
                    matrix[j-1][i] = '0' 
        ls.append(n)
    for i,v in enumerate(ls):
        for k in range(v):
            matrix[k].pop(i)
            matrix[k].insert(i,nexts[i].pop(0))




if __name__ == '__main__':
    n = int(input())
    matrix = [list(input()) for _ in range(8)]
    nexts = [list(input()) for _ in range(8)]
    taps = []
    for _ in range(n):
        s = input().split()
        taps.append([int(s[0])-1, int(s[1])-1, s[2]])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for x,y,z in taps:
        ans = 0
        if z == 'w':
            dfs(matrix,x,y,matrix[x][y])
            change_w()
            print(ans)
        elif z == 's':
            dfs(matrix,x,y,matrix[x][y])
            change_s()
            print(ans)
        elif z == 'a':
            dfs(matrix,x,y,matrix[x][y])
            change_a()
            print(ans)
        else:
            dfs(matrix,x,y,matrix[x][y])
            change_d()
            print(ans)



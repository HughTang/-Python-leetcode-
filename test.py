# if __name__ == '__main__':
#     nums = list(map(int, input().split()))
#     vals = list(set(nums))
#     vals.sort()
#     if len(vals) < 3:
#         print(max(vals))
#     else:
#         print(vals[-3])

def dfs(a, b, num):
    if a >= b:
        return num % 2 == 1
    if num % 2 == 1:
        return dfs(a*2, b, num+1) and dfs(a+1,b,num+1)
    return dfs(a*2, b, num+1) or dfs(a+1,b,num+1)


if __name__ == '__main__':
    t = int(input())
    ans = list()
    for _ in range(t):
        x,y = map(int, input().split())
        if dfs(x,y,0):
            ans.append('kou')
        else:
            ans.append('yukari')
    for x in ans:
        print(x)
        

 
def printV(nums, V):
    for i in nums:
        V.append(0)
        if i > len(V):
            for j in range(len(V)):
                V[j] = 1
        else:
            for k in range(len(V) - i, len(V)):
                V[k] = 1
    return V


n = int(input(''))  # 进行n次测试
for i in range(n):
    V = []
    length = int(input())
    l = list(map(int, input().split()))
    res = printV(l, V)
    for m in res:
        print(m, end='')

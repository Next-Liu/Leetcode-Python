n = int(input(""))
l = list(map(int, input().split()))
if n < 3:
    print(0)
else:
    presum = [0 for _ in range(n + 1)]
    for i in range(n):
        presum[i + 1] = presum[i] + l[i]
    if presum[n] % 3 != 0:
        print(0)
    else:
        avg = presum[n] // 3
        a = avg
        b = avg * 2
        cns = 0
        res = 0
        for j in range(2, n):
            if presum[j - 1] == a:  # 等于avg的个数
                cns += 1
            if presum[j] == b:
                res += cns  # 等于avg的位置必须在等于avg*2的位置之前
        print(res)

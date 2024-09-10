# 以threshold为阈值，能分为几组
def countGroup(threshold, l):
    num = 1
    left = right = 0
    while right < len(l):
        if l[right] - l[left] <= threshold:
            right += 1
        else:
            left = right
            num += 1
    return num


i = input("")
a = [int(x) for x in i.split(" ")]
n = a[0]
k = a[1]
j = input("")
l = list(map(int, input().split()))  # 一行输入多个数字 int函数用于将输入的字符串转换成整数
l.sort()
right = l[-1] - l[0]
left = 0
p = (right + left) // 2
while right >= left:
    mid = (left + right) // 2
    if countGroup(mid, l) > k:
        left = mid + 1
    else:
        right = mid - 1
        p = mid
print(p)

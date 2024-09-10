if __name__ == '__main__':
    width = int(input("请输入宽:"))
    height = int(input("请输入高:"))
    big = max(width, height)
    small = min(width, height)
    gap = big - small
    count = 0
    while gap != 0:
        count += 1
        big = max(gap, small)
        small = min(gap, small)
        gap = big - small
    print(count + 1)

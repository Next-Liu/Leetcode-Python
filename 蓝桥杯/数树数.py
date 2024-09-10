i = input("")
a = [int(x) for x in i.split(" ")]
n = a[0]
q = a[1]
request = []
for i in range(q):
    request.append(input(""))
res = []
val = 1
for j in request:
    for k in j:
        if k == 'L':
            val = val * 2 - 1
        else:
            val = val * 2
    res.append(val)
    val = 1
for ans in res:
    print(ans)
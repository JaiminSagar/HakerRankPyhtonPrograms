ps = []
# no = []
# naam = []
flag = 0
ans = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    ps.append([name, score])
    # no.append(score)
    # naam.append(name)


def sortSecond(val):
    return val[1]


ps.sort(key=sortSecond)
print(ps)
for i in range(1, len(ps)):
    if ps[0][1] < ps[i][1] and flag == 0:
        ans.append(ps[i])
        flag = 1
    elif len(ans) != 0 and ans[0][1] == ps[i][1]:
        ans.append(ps[i])

for j in ans:
    print(j[0])
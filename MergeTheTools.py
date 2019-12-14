def merge_the_tools(string, k):
    splitStr = []
    i = 1
    n = 1
    z = len(string)/k
    while i <= z:
        s = ''
        for j in range(n, len(string)+1):
            s = s + string[j-1]
            if j % k == 0:
                #print(s)
                splitStr.append(s)
                break
        i += 1
        n += k
    #print(splitStr)
    if k == 1:
        for x in string:
            print(x)
    else:
        for p in splitStr:
            s = ''
            for q in range(0, k):
                for r in range(0, k):
                    if q == r:
                        continue
                    if p[q] != p[r] and p[q] not in s:
                        s = s + p[q]
            print(s)


string, k = input(), int(input())
merge_the_tools(string, k)
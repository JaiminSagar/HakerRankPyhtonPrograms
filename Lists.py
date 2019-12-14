N = int(input())
l = []
for j in range(N):
    ip = list(input().split())
        #print(ip)
    if ip[0] == "insert":
        l.insert(int(ip[1]), int(ip[2]))
    elif ip[0] == "print":
        print(l)
    elif ip[0] == "remove":
        l.remove(int(ip[1]))
    elif ip[0] == "append":
        l.append(int(ip[1]))
    elif ip[0] == "sort":
        l.sort()
    elif ip[0] == "pop":
        l.pop()
    elif ip[0] == "reverse":
        l.sort(reverse = True)
        ip = []

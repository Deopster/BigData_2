n = m = int(input())
rez = [[ '1' if (i + j)==n-1 else '0' for j in range(m)] for i in range(n)]
for i in rez:
    print(*i)



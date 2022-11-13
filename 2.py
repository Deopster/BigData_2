s=int(input())+1
print(*[x for x in range(1,s) for m in range(x)][:s-1] )
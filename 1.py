s = m = 0
rm=lambda m,s,x:(x*x+m,x+s)
while True:
    m , s = (rm(m,s,int(input())))
    if s==0:
        print(m)
        break

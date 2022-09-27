def NumberArrow(): 
    n = int(input())
    for i in range(2*n):
        if i<=n:
            print(*range(1,i+1), sep = ',')
        else:
            print(*range(1,(2*n-i+1)), sep = ',')
NumberArrow()

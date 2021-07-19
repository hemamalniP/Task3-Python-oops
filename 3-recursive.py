def calc(n):
    if n:
        return n+calc(n-1)
    else:
        return 0
        
sum1=calc(10)
print(sum1)

def addDigits(num):
    while num>=10:
        num=sum(map(int,str(num)))
    return num
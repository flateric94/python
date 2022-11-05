def nombredor():
    x=1.6
    x1=1.61
    while x-x1<10**20:
        x=x1
        x1=x-(x**2 -x-1)/(2*x-1)
        x1=round(x1,20)
        return(x1)

print(nombredor())
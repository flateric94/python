def fibonacci(N):
    U=[0]*N
    U[0]=1
    U[1]=1
    for i in range(2,N):
        U[i]=U[i-1]+U[i-2]        
    return(print(U))

print(fibonacci(10))
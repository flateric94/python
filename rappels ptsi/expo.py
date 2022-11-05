def puiss2(x,n):
    P=1
    u=x
    m=n
    while m>0:
        if m%2==1:
            P=P*u
        u=u*u
        m=m//2
    return(P)

print(puiss2(2,3))


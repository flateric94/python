#tri par sélection

def tri_par_selection(L):
    n=len(L)
    E=[]
    for i in range(n):
        m=min(L)
        E.append(m)
        L.remove(m)
    return(E) 

print(tri_par_selection([1,0,34,-56,90,23,9]))

#tri par bulle

def tri_par_bulle(L):
    temp=0
    n=len(L)
    for i in range(n):
        for j in range(i+1,n):
            if L[i] > L[j]:
                temp=L[i]
                L[i]=L[j]
                L[j]=temp
    return(L)

print(tri_par_bulle([1,0,34,-56,90,23,9]))

#tri rapide

def fusion(L1,L2):
    if L1==[]:
        return(L2)
    elif L2==[]:
        return(L1)
    elif L1[0]<L2[0]:
        return [L1[0]]+fusion(L1[1:],L2)
    else:
        return [L2[0]]+fusion(L1,L2[1:])

def tri_par_fusion(L):
    n=len(L)
    if n<2:
        return L
    else:
        pivot=n//2
    return fusion(tri_par_fusion(L[:pivot]),tri_par_fusion(L[pivot:]))

print(tri_par_fusion([1,0,34,-56,90,23,9]))


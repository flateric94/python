#question1) verifier si a est une permutation => verifier termes à termes

def testperm(a):
    n=len(a)
    for i in range(n):
        # print(a[i])
        if a[i]<0 or a[i]>len(a):
            return("erreur")
        for j in range(i+1,n):
            # print(i,j)
            if a[i]==a[j]:
                return("erreur")
        
    return("c'est bon")

print(testperm([1,2,3]))
print(testperm([6,4,3,1,2,5]))
print(testperm([1,1,0]))
print(testperm([2,0,1,2]))
print(testperm([0,2,3,6,3]))
print(testperm([-1,3,8,4,0,78]))

#question2)

# def testpermoptial(a):
#     n=len(a)
#     l=[0]*n
#     repere=a[i]
#     for i in range(n):
        


    
    


# print(testpermoptial([1,2,3,4]))
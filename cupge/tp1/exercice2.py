#question1) verifier si a est une permutation => verifier termes à termes

def testperm(a):
    n=len(a)
    for i in range(n):
        # print(a[i])
        if a[i]<0 or a[i]>n-1:
            return("erreur")
        for j in range(i+1,n):
            # print(i,j)
            if a[i]==a[j]:
                return("erreur")        
    return("c'est bon")

# print("#### testperm ####")
# print(testperm([1,1,2])) 
# print(testperm([0,1,2]))
# print(testperm([0,4,3,1,2,5]))
# print(testperm([1,1,0]))
# print(testperm([2,0,1,2]))
# print(testperm([0,2,3,6,3]))
# print(testperm([-1,3,8,4,0,78]))
# print("#### fin testperm ####")

#question2) on introduit un tableau l dans lequel on va se souvenir des éléments déjà utilisés dans la construction d'une permutation
# ici : avec interruption immédiate
def testpermoptial(a):   
    n=len(a)
    l=[0]*n
    for i in range(n):
        # print(a[i])
        if a[i]<0 or a[i]>n-1:
            return("erreur : le terme est en dehors des valeurs acceptables")
        if l[a[i]]==0:
            # print(l[a[i]])
            l[a[i]]=1
            # print(l[a[i]])
        else:
            return("erreur : j'ai trouvé le premier doublon")
    return("correct")

# print("#### testpermoptial ####") 
# print(testpermoptial([1,1,3,4]))
# print(testpermoptial([2,3,1,2]))
# print(testpermoptial([1,2,4,45,5]))
# print("#### fin testpermoptial ####")

# ici : avec comparaison finale
def testpermoptial2(a):   
    n=len(a)
    l=[0]*n
    for i in range(n):
        # print(a[i])
        if a[i]<0 or a[i]>n-1:
            return("erreur : le terme est en dehors des valeurs acceptables")
        if l[a[i]]==0:
            # print(l[a[i]-1])
            l[a[i]]=1
            # print(l[a[i]-1])
        else:
            l[a[i]]=0
    if l==[1]*4:
        return("correct : pas de doublons")
    else:
        # print(l)
        return("incorrect : il y a au moins un doublon")

# print("#### testpermoptial2 ####")
# print(testpermoptial2([0,0,2,3]))
# print("#### fin testpermoptial2 ####")

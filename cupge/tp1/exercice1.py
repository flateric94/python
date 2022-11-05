#question1) écrire un algorithme power utilisant une boucle pour calculer x^n, x et n en entrée

def power(x,n):
    valeur=1
    for i in range(n):
        valeur=valeur*x
        # print(i,valeur)
    return(valeur)

# print("##### power #####")
# print(power(3,3)) #renvoit 27
# print(power(4,2)) #renvoit 16
# print(power(2,8))
# print("### fin power ####")

#question2) dans le cas où n puissance de 2, simplifier algorithme
def power2(x,k):
    valeur=x
    for i in range(k):
        valeur=valeur*valeur
    return(valeur)

# print("##### power2 #####")
# print(power2(2,3))
# print("### fin power2 ####")

#question3) tout nombre n peut s'écrire sous forme Somme(ak2^k) avec ak=1ou0

def puissance(x,n):
    valeur=1
    while n>0:
        if n%2==1: 
            valeur=valeur*x
        x=x*x
        n=n//2
    return(valeur)

# print("#### puissance ####")
# for i in range(0,9) :
#     print("2^{0}={1}".format(i,puissance(2,i)))
# print("#### fin puissance ####")

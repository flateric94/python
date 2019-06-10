def devineage():
    min=0
    max=100
    while max!=min+1:
        age=(min+max)/2
        age2=int(age)
        print("l'individu à " + str(age2) + "ans ?")
        resultat=input("reponse: ")
        res=int(resultat)
        if res==1:
            min=age2
        elif res==-1:
            max=age2
        elif res==0:
            break
        else:
            continue
    if res==0:
        print("la machine gagne toujours")
    else:
        print("tu es entrain de mentir")
    return

print(devineage())


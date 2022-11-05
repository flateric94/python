#ordre lexicographique

def ordrelexico(l1,l2):
    a=[l1,l2]
    L=sorted(a)
    print(L)
    if L[0] == l1:
        return True
    else:
        return False

print(ordrelexico("alban", "Alban"))
print(ordrelexico("Alban", "alban"))
print(ordrelexico("kiwi", "fraise"))
print(ordrelexico("fraise", "kiwi"))

#chaine préfixe

def prefixe(l1,l2):
    i = 0
    n,p = len(l1),len(l2)
    if n >= p:
        return False
    else: 
        while i < n:
            if l1[i] != l2[i]:
                return False
            else:
                i += 1
        return True


# print(prefixe("bon" , "bonjour"))
# print(prefixe("enfh" , "enchanté"))
# print(prefixe("ban" , "kanane"))

#chaine suffixe

def suffixe(l1,l2):
    i = 0
    n,p = len(l1),len(l2)
    if n > p:
        return False
    else: 
        while i < n:
            if l1[i] != l2[p - n + i]:
                return False
            else:
                i += 1
        return True    

# print(suffixe("age" , "codage"))
# print(suffixe("ment", "gentillement"))
# print(suffixe("ade" , "embrassade"))
# print(suffixe("ade", "deconnad"))



def informations(l):
    n=len(l)
    moyenne=0
    for i in range(n):
        moyenne=moyenne+l[i]
    moyenne=moyenne/n
    return(min(l),max(l),moyenne)

print("#### informations ####")
print(informations([1,2,3,4]))
print("#### fin informations ####")


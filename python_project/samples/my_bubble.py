__author__ = 'Vlad'
sort = input("Input some array to sort: ")
z = len(sort)
issort = True
while (issort == True):
    for i in range(z-1):
        if sort[i] > sort[i+1]:
            issort = True
            sort[i],sort[i+1] = sort[i+1],sort[i]
        else:
            issort = False
z-=1

print z, sort
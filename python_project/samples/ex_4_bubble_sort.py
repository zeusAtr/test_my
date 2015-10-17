__author__ = 'Vlad'
import random
l = [random.randint(1,100) for i in range(10)]
print l

# r = len(l)
# sort = True
# while sort:
#     sort = False
#     for i in range(r-1):
#        if l[i] > l[i + 1]:
#         sort = True
#         l[i],l[i+1]= l[i+1],l[i]
#     r -= 1
# print l

######################
# from algorithms.sorting import bubble_sort
#
# my_list = bubble_sort.sort(l)
# print

######################
def sort (for_sort):
    z = len(for_sort)
    while z>0:
        for i in range(z-1):
            if for_sort[i]>for_sort[i+1]:
                for_sort[i+1],for_sort[i] = for_sort[i],for_sort[i+1]
            i+=1
        z-=1

    return (for_sort)

print sort(l)
######################

















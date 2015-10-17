__author__ = 'Vlad'

def repeat_least(l1, l2=[1,2,3,4,5]):
    a = set(l1) & set(l2)

    return 'The intersect elements are:', a

print repeat_least([8,4,9,1],[3,8])
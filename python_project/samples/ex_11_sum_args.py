__author__ = 'Vlad'

def sum_arg(*args):
    a = len(args)
    if a == 2:
        rez = 2
        descr ='There are two values in argument'
    elif a < 2:
        rez = -1
        descr = 'There are less two values in argument'
    else:
        rez = 0
        descr = 'There are more two values in argument'
    return rez,descr

print sum_arg(3,3,4)


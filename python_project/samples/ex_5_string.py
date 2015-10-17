__author__ = 'Vlad'

import random
l = [random.sample(range(10),5) for i in range(3)]
print l

sum = sum(l[0][-3:])
print "summ three last value of first array:", sum

min_value = min(l[0][1],l[1][1],l[2][1])
print "min value of second value for all arrays",min_value

total_max0 = max(l[0])
total_max1 = max(l[1])
total_max2 = max(l[2])
total_max = max(total_max0,total_max1,total_max2)
print "total max for all arrays", total_max

for i in range (len(l)):
    if 4 in l[i]:
        print "index of sub-array where 4 occured is", l.index(l[i])
    else:
        print "4 is not in the list", l.index(l[i])

    # import random
    #
    # sample_list = [random.sample(range(10), 3) for i in range(3)]
    # print sample_list
    #
    # sum_first = sum(sample_list[0][-2:])
    # min_int_second = min(i[1] for i in sample_list)
    # max_int_matrix = max(max(x) for x in sample_list)
    #
    # four_index = []
    # for index, value in enumerate(sample_list):
    #     if 4 in value:
    #         four_index.append(index)
    #
    # print "last two elements is: %s" % sum_first
    # print "min of second row is: %s" % min_int_second
    # print "max of whole array is: %s" % max_int_matrix
    # print "index of sub-array where 4 occured is: %s" % four_index
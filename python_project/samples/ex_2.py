# __author__ = 'Vlad'
# l = []
# a = 1,2,"3",4,"5"
# for item in a:
#     l.append(int(item)*3)
#     print l[int(item)-1]+10

#
# score = float(raw_input("Enter scode between 0.0 and 1.0:"))
#
# while score > 1:
#     print "ERROR"
#     exit(1)
#
# if score >=0.9:
#     print "A"
# elif score >=0.8:
#     print "B"
# elif score >=0.7:
#     print "C"
# elif score >=0.6:
#     print "D"
# else:
#     print "F"


largest = 0
smallest = 0

while True:
    try:
        num = (raw_input("Enter a number: "))
        if num == "done":
             break
        elif num == 'a':
            raise ValueError
        if num > largest:
            largest = num
        elif num<smallest:
            smallest = num

        print num

    except ValueError:
        print "Invalid input"
print "Maximum is", largest
print "Minimum is", smallest


# __author__ = 'Vlad'
# l = []
# a = 1,2,"3",4,"5"
# for item in a:
#     l.append(int(item)*3)
#     print l[int(item)-1]+10

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


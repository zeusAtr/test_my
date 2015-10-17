__author__ = 'Vlad'
import sys

def main():
    if len(sys.argv[0:]) == 1:
        print "Imput some string with numbers"
        exit(1)
    elif len(sys.argv[0:]) == 2:
        print "You should input at least two arguments"
        exit(1)

    list = filter(str.isdigit,(sys.argv[1: ]))
    order_int = sorted(map(int,list))

    print 'Sum two of biggest numbers is %s' % (sum(order_int[-2:]))
if __name__ == '__main__':
    main()



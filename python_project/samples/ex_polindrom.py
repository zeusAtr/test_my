__author__ = 'Vlad'
def func():
    import sys
    try:
        a = sys.argv[1:]
        str_analyze = a[0].lower().replace(" ", "")
        assert len(a) == 1, 'Something was WRONG. You should input at least one argument'
        # print str_analyze, str_analyze[::-1]

        if str_analyze == str_analyze[::-1]:
            print "YES! Hey, it's a polindrom!!"
        else:
            print 'NO =( It is not a polindrom, man...'

    except IndexError:
        print 'Something was WRONG. You should input at least one argument'

if __name__ == '__main__':
    func()
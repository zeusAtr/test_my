__author__ = 'Vlad'
# a = raw_input (" Enter n USD or n EUR")
# total = a.split(' ')
# tr = {"USD":"0.81","EUR":"1.22"}
#
# if (total[1] == 'USD'):
#      s = float(total[0]) * float(tr['USD'])
#      ute = round(s,2)
#      ute1 = str(ute)
#
# if ute1[-2::] == '.0':
#      print ute1[:-2:], "EUR"
# else:
#      print ute1[:-3:], "EUR and",ute1[-2::], "CENT"
def mfunc():
    a = raw_input(' Enter USD or EUR to convert: ')
    enter_cur =  a.split()[1]
    reverece_enter_cur = ''
    value = a.split()[0]
    currncy = {"USD": 0.81, "EUR": 1.22}

    if enter_cur == "USD":
        reverece_enter_cur = "EUR"
    elif enter_cur == "EUR":
        reverece_enter_cur = "USD"

    rez = round((float(a.split()[0]) * currncy[enter_cur]), 2)


    cop = int( str(rez).split('.')[1] )
    without_cop = int( str(rez).split('.')[0] )

    if cop == 0:
       print int(rez), reverece_enter_cur
    else:
       print without_cop,reverece_enter_cur,'and',cop,'CENT'

if __name__ == '__main__':
    mfunc()

"""
def main():
    text = raw_input("Please type yor text: ")

    amount = float(text.split()[0])
    currency = text.split()[1]
    print currency
    rates = {"USD":0.81, "EUR":1.22}

    converted_currency = "USD" if currency == "EUR" else "EUR"
    to_be_paid = round(amount*rates[currency],2)
    cents = int(str(to_be_paid).split(".")[1])

    if cents == 0:
        print "%d %s" % (amount*rates[currency], converted_currency)
    else:
        print "%d %s and %d cents" % (amount*rates[currency], converted_currency, cents)

if __name__ == '__main__':
    main()
"""



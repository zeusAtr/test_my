__author__ = 'Vlad'
from convertors_pak import money,time_my

q = float (raw_input("Enter some value in mili seconds: "))
print '%d mili seconds is a %f minutes' %(q,time_my.cc(q))
money.mfunc()
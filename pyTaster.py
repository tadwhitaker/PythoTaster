from random import randint
import math

#
# list = ['Tad', 'Terry', 'Fountain']
#
# for i in list: print 'Name: ', i
#
# print (randint(0, 100))
#
# bike = "Haro"
#
# def tester(z):
#     print z
#     return
#
# tester(bike)


num = 99

def single(z):
    list = map(int, str(z))
    sum = str(list[0] + list[1])
    if (len(sum) < 2):
        print "The answer " + sum + " is 1 digit long."
    else:
        single(sum)
    return

single(num)
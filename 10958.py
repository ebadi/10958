
from multiprocessing import Pool as ThreadPool
import sys
import math

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]


def toOp(n,Ncount, OPcount):
    x = toStr(n,OPcount)
    x = x.rjust( (Ncount ), '0')
    mapping = [ ('0', '+'), ('1', '-'), ('2', '|'), ('3', '/'), ('4', '*'), ('5', '^') ]
    for k, v in mapping:
        x = x.replace(k, v)
    return x

def interleave2(s, t, res, i, j, lis):
    if j >= i and j!=0 : # remove invalid expressions
        return

    if i == len(s) and j == len(t):
        lis.append(res)
        return
    if i < len(s):
        interleave2(s, t, res + s[i], i + 1, j, lis)
    if j < len(t):
        interleave2(s, t, res + t[j], i, j + 1, lis)

# https://en.wikipedia.org/wiki/Reverse_Polish_notation
# Reverse Polish notation (to avoid paranthesis)
def parse_rpn(expression):
    stack = []

    for val in list(expression):
        if val in ['+', '-', '*', '/', '^', '|']:
            op1 = stack.pop()
            op2 = stack.pop()
            #print ( "op2=", op2, val, "op1=" , op1)
            if (op1 > 9999999 or  op2 > 9999999 or op1 < -9999999 or  op2 < -9999999):
                raise
            if val=='-': result = op2 - op1
            if val=='+': result = op2 + op1
            if val=='*': result = op2 * op1
            if val=='^':
                if abs(op2 + op1) < 15 or abs(op2) ==1 or abs(op1) ==1:
                    result = pow (op2,op1)
                else :
                    raise
            if val=='|':
                result = int(str(op2) + str(op1))
            if val=='/':
                if op2 % op1 == 0:
                    result = op2 // op1
                else :
                    raise
            stack.append(result)
        else:
            stack.append(int(val))
    if (len(stack) ==1 ):
        rx = stack.pop()
        return rx
    else :
        raise



nc = 10
oc = 6
# 123456789
s = "123456789"

# Parker's solution with flexible concatenation
# (1*(2|3))+(((((4*5)*6)|7) + 8 )*9)
# print parse_rpn("123|*45*6*7|8+9*+") # 10958
# exit()
# interleave2(s,"+-/*^+-*", "", 0, 0, l)
# print (l)
# Postfix to infix:
# http://www.mathblog.dk/tools/infix-postfix-converter/
# try :
#     print parse_rpn("512+4*+3-")  #"(5 + ((1 + 2) * 4)) - 3"    = 14
#     print parse_rpn("512+4^+2/")  #"(5 + ((1 + 2) ^ 4)) / 2"    = 14
#     print parse_rpn("512*4^+3/")  #"(5 + ((1 * 2) ^ 4)) / 3"    = 7
#     print parse_rpn("12|34|+")    #12 + 34  = 46
#     print parse_rpn("512*4^+2/")  #"(5 + ((1 * 2) ^ 4)) / 2"    = error
# except:
#     print "error"
# exit()



def check(i):
    l = []     # l HAS TO BE A LOCAL VARIABLE
    t = toOp(i,nc-2, oc)
    interleave2(s,t, "", 0, 0, l) # len(l) : 1430
    for x in l :
        try :
            v = parse_rpn(x)
            if v == 10958:
                print ("======= [ Founded ] ======")
                print ("=========================")
                print (x,v)
                print ("=========================")
                sys.stdout.flush()
        except:
            continue


# Sequential
#for k in range(0, pow(oc,nc)):
#    check (k)

# Parallel
counter = 0
startFrom = int(sys.argv[1])
threads = int(sys.argv[2])
for k in range(startFrom, startFrom+ pow(oc,nc-1),threads):
    pool = ThreadPool(threads)
    counter = counter +1
    pool.map(check, range(k, k+threads))
    if counter > 100 :
        print (k)
        sys.stdout.flush()
        counter = 0
    pool.close()
    pool.join()

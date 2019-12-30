# -*- coding: utf-8 -*-
# Funny formula
import math
import sys
def Eulerproduct(x):
    s = 0
    for i in range(1, x[0]):
        s += 1/(x[1]**i)
    return str(s)+" and ζ("+str(x[1])+") are equal"

def oiler():
    return "e^(i*n)+1=0"

def Fibonacci(x):
    n = math.sqrt(5)
    return "F(" + str(x) + ") = " + str(int(1/n*(((1+n)/2)**x - ((1-n)/2)**x)))

def pi(x):
    s = 0
    for i in range(1, x):
        s+=1 / i ** 2
    return "pi=" + str(math.sqrt(s*6))

def HN(x):
    s = 0
    for i in range(1, x):
        s+= 1 / i
    return s

def PP(p):
    return [p[0] ** 2 - p[1] ** 2, 2 * p[0] * p[1], p[0] ** 2 + p[1] ** 2]

if __name__ == "__main__":
    print("Welcome to Funny tormula")
    while True:
        print("Which would you choose?")
        print("1.Euler product")
        print("2.oiler")
        print("3.Fibonacci")
        print("4.pi")
        print("5.Harmonic number")
        print("6. Primitive Pythagoras")
        print("7.quit")
        a = int(input())
        print(a)
        if a == 7:
            print("thank you")
            sys.exit()
        elif a == 6:
            print("Enter two prime numbers(space separated):")
            ret = PP(list(map(int,input().split())))
            print(str(ret[0])+","+str(ret[1])+","+str(ret[2]))
        elif a == 5:
            print("Enter precision:")
            print(HN(int(input())))
        elif a == 4:
            print("Enter precision:")
            print(pi(int(input())))
        elif a == 3:
            print("What order do you want:")
            print(Fibonacci(int(input())))
        elif a == 2:
            print(oiler())
        elif a == 1:
            print("Enter two numbers:")
            print(Eulerproduct(list(map(int,input().split()))))
        print("---------------------------------------------------------")

import sys
import math

a,b = map(int, sys.stdin.readline().strip().split())
c,d = map(int, sys.stdin.readline().strip().split())

def LCM(a, b):
    return a * b // math.gcd(a, b)


A = a*d + c*b
B = b*d

print(A//math.gcd(A,B), B//(math.gcd(A,B)))
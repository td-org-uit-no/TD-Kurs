#!/usr/bin/python3

from math import sin, pi
import time

N = 80

def f(x):
    A, f = 2, 4
    return A*sin(x*f*pi)

print("    x                 f(x)")
for i in range(N):
    x = time.clock_gettime(time.CLOCK_BOOTTIME)
    print(f"f({x:.3f}) = {f(x):9.3f}")
    time.sleep(1/20)


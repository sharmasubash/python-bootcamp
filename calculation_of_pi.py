# -*- coding: utf-8 -*-
# Create the Function to calculate PI using Ramanujam Series

from decimal import Decimal

def fact(n):
    fact = 1
    if n == 0:
        return fact;
    else:
        while (n>=1):
            fact = n * fact
            n = n-1   
        return fact
    


def ramu_pi(num):
    constant = (8**(0.5))/9801 ;
    z = 0
    for n in range(num):
        x = float(constant*(((fact(4*n))/(fact(n)**4)) * ((26390*n) + 1103)/396**(4*n)))
        z = z + x;
    return z

1/Decimal(ramu_pi(2000))
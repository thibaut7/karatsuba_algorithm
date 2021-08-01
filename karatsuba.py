# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:46:11 2021

@author: thibaut
function karatsuba to multiply 2 integers 
"""
def karatsuba(num1, num2):
#if it's one-digit numbers just multiply

    if len(str(num1))==1 and len(str(num2))==1:
        return num1*num2
# write the numbers in this form:10^(n/2)a+b where n is max lenght of the two
# integers
# extract lenght   
    num1_lenght = len(str(num1))
    num2_lenght = len(str(num2))
# Extract the maximum lenght
    n = max(num1_lenght, num2_lenght)
    n2 = round(n/2)
    
# num1 = (10^n2)a + b and num2 = (10^n2)c + d 
    a = num1//(10**n2)
    c = num2//(10**n2)
    b = num1%(10**n2)
    d = num2%(10**n2)
    
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
# ad+bc=(a+b)(c+d)-ac-bd
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    return (10 ** (2*n2))*ac + (10 ** n2)*ad_plus_bc + bd
#Example
print(karatsuba(1524, 1254))
    
    
    
    
    
    
        
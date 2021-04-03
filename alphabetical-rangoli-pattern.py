# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 16:06:01 2021

@author: Parvish
"""
def print_rangoli(size):
    # your code goes here
    for i in range(size-1,0,-1):
        for j in range(i*2,0,-1):
            print("-",end="")
        for k in range(97+size-1,97+i-1,-1):
            print(chr(k),end="-")
        for l in range(97+i+1,97+size):
            print(chr(l),end="-") 
        for j in range(i*2-1,0,-1):
            print("-",end="")
        print()
        
    for i in range(0,size*2,2):
        for j in range(0,i):
            print("-",end="")
        for k in range(97+size-1,96+int(i/2),-1):
            if(k==96+int(i/2)+1):
                print(chr(k),end="")
            else:
                print(chr(k),end="-")
        for l in range(98+int(i/2),97+size):
            print("-"+(chr(l)),end="")
        for j in range(0,i):
            print("-",end="")
        print()
        
def main():
    n=int(input())
    print_rangoli(n)
    
main()
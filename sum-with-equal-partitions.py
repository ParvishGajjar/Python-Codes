# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 11:42:27 2020

@author: Parvish
"""

# Finds sum with equal partition of the list
def equalPartitionSums(l):
    listLength=len(l)
    l1=[]
    l2=[]
    for i in range(listLength,0,-1):
        for j in range(0,listLength-1):
            l1.append(l[j])
        for k in range(listLength-1,len(l)):
            l2.append(l[k])        
        if sum(l1) == sum(l2):
            print('List 1: ', l1, '\nList 2: ',l2,'\nSum: ', sum(l1))
            break;
        elif sum(l2)<sum(l1):
            l1=[]
            l2=[]
            listLength-=1
        else:
            print('No such partition possible')
            break;
            
# Main Function
def main():
    n=int(input('Enter the length of your list: '))
    ls=[]
    l=[]
    for i in range(0,n):
        l=int(input())
        ls.append(int(l))
    ls.sort()
    equalPartitionSums(ls)

# While loop, in order to ask user for retry
while 1:
    main()
    ta=input('Try again? (Y/N)')
    if(ta.lower() == 'n'):
        break
  
"""
Example:

#1  Enter the length of the list: 6
    1
    1
    2
    3
    3
    10
    
    #Output will come as,
    
    List 1: [1,1,2,3,3]
    List 2: [10]
    Sum: 10
    
#2  Enter the length of list: 5
    1
    2
    3
    4
    5
    
    # Output will come as,
    
    No such partitions possible
"""
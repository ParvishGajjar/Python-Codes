# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:18:09 2021

@author: Parvish
"""

# Code Chef Challenge - CHEFMAS

from itertools import permutations  

def unique(l):
    unique_list = []
    for x in l:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def recursiveDistribution(ls,maxSweets,current_values,flag,sweets,temp_values,distribution):
    if(len(ls[flag:])>1):
        for i in ls[flag:flag+1]:
            test_values=temp_values[:]
            for k in range(maxSweets,0,-1):
                if sum(current_values)<sweets:
                    current_values[i]+=k
                    temp_values=current_values[:]
                    flag+=1
                    flag,distribution = recursiveDistribution(ls,maxSweets-k,current_values,flag,sweets,temp_values,distribution)
                    current_values=test_values[:]
        return flag-1,distribution
    
    else:
        current_values[ls[flag]]+=maxSweets
        if sum(current_values)==sweets:
            distribution.append(current_values)
        return flag-1,distribution
        

def recursiveDistributionCaller(ic,sweets,current_values,distribution,ac_list):
    maxSweets=sweets-sum(current_values)
    for i in ic:
        flag=0
        if len(i)>1:
            for j in i[flag:flag+1]:
                for k in range(maxSweets,0,-1):
                    if sum(current_values)<sweets:
                        current_values[j]+=k
                        flag+=1
                        temp_values=current_values[:]
                        flag,distribution=recursiveDistribution(i,maxSweets-k,current_values,flag,sweets,temp_values,distribution)
                        current_values=ac_list[:]

        else:
            current_values[i[0]]+=maxSweets
            if sum(current_values)==sweets:
                distribution.append(current_values)
            current_values=ac_list[:]
            
def main():
    try:
        tc=int(input())
        if tc<1 or tc>100:
            raise Exception('Test cases should be between 0 to 100')
        output=[]
        for i in range(0,tc):
           
            sweets,children=input().split(' ')
            children=int(children)
            sweets=int(sweets)

            if((children<1 or children>sweets or children>pow(10,5)) or (sweets<1 or sweets>pow(10,5))):
                raise Exception('Children and sweets must be in following format, 1<=children<=sweets<=10^5')
    
            ac_list=input().split(' ',maxsplit=children)
            
            if  len(ac_list)>children:
                ac_list.pop(children)
                
            ac_list = [int(i) for i in ac_list] 
            
            for i in ac_list:
                if i>pow(10,5) or i<0:
                    raise Exception('Goodness count must be between 0 to 10^5')
                    
            if sum(ac_list)>sweets:
                output.append(0)
        
            elif sum(ac_list)==sweets:
                output.append(1)
        
            else:
                current_values=ac_list[:]
                distribution=[]
                index_combination=[]
                indexes=[idx for idx,val in enumerate(current_values)]
                
                for i in range(1,len(current_values)+1):
                    perm = permutations(indexes, i)
                    for i in list(perm):
                        index_combination.append(i)

                recursiveDistributionCaller(index_combination,sweets,current_values,distribution,ac_list)
                distributed_probability=unique(distribution)
                output.append(len(distributed_probability))
                
        for i in output:
            print(i)
        
    except Exception as e:
        print(e)
    
main()
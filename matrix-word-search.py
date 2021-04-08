# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 22:21:33 2021

@author: Parvish
"""

"""
Question: Given an m x n grid of characters board and a string word, return true if word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

"""
Answer
"""

word_list=[]
outputs=[]

# Static Input

matrix_data=[['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
search_word="SEE"

# Dynamic Input

# rows,cols=[int(x) for x in input('Enter rows and columns: ').split()]
# for i in range(rows):
#     j=input().split(' ', maxsplit=cols)
#     matrix_data.append(j)
# search_word+=input('Enter search word: ')
# print("\n\nMatrix Data\n", matrix_data,"\nSearch word: ", search_word)

def unique(l):
    unique_list = []
    for x in l:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def recursiveFinder(word, row, col, data, outputs, index):
    if(row+1<=len(data)-1 and data[row+1][col]==word[0]):
        outputs[index].append([word[0],row+1,col])
        if(len(word)==1):
            found=True
        else:
            found=recursiveFinder(word[1:],row+1, col, data, outputs, index)
        if(found):
            return True
    if(col+1<=len(data[row])-1 and data[row][col+1]==word[0]):
        outputs[index].append([word[0],row,col+1])
        if(len(word)==1):
            found=True
        else:
            found=recursiveFinder(word[1:],row, col+1, data, outputs, index)
        if(found):
            return True
    if(row-1>=0 and data[row-1][col]==word[0]):
        outputs[index].append([word[0],row-1,col])
        if(len(word)==1):
            found=True
        else:
            found=recursiveFinder(word[1:],row-1, col, data, outputs, index)
        if(found):
            return True
    if(col-1>=0 and data[row][col-1]==word[0]):
        outputs[index].append([word[0],row,col-1])
        if(len(word)==1):
            found=True
        else:
            found=recursiveFinder(word[1:],row, col-1, data, outputs, index)
        if(found):
            return True
    return False

def solution(matrix_data,search_word):
    for i in search_word:
        word_list.append(i)
    for i in range(len(matrix_data)):
        for j in range(len(matrix_data[i])):
            outputs.append([])
            if(matrix_data[i][j]==word_list[0]):
                outputs[i+j].append([word_list[0],i,j])
                output_index=i+j
                if(len(word_list)==1):
                    found=True
                else:
                    found=recursiveFinder(word_list[1:], i, j, matrix_data, outputs, output_index)
                if(found):
                    return True
    return False

def main():
    output=solution(matrix_data,search_word)
    flag=0
    if(output):
        for i in range(len(outputs)):
            outputs[i]=unique(outputs[i])
        for i in outputs:
            if(len(i)==len(word_list)):
                flag=1
            if(flag):
                print('true')
                break
        if(flag==0):
            print('false')
    else:
        print('false')

main()

"""
Example:
    
    #1 Matrix Data: [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
       Search Word: SEE
       
       Output: true
      
    #2 Matrix Data: [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
       Search Word: ABCCED
       
       Output: true
       
    #3 Matrix Data: [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
       Search Word: ABCB
       
       Output: false
"""
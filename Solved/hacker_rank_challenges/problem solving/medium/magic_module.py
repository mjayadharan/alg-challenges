#!/usr/bin/env python
# coding: utf-8

# ## Class to create magic square of order 3.
# ### Manu Jayadharan

# In[13]:


import itertools
class GiveMagicSquare_3:
    def __init__(self):
        self.magic_square_list=[]
        self.square_list=[]
        
    def diag_sum(self,arr):
        return arr[0][0]+arr[1][1]+arr[2][2]
    
    def sec_diag_sum(self,arr):
        return arr[0][2]+arr[1][1]+arr[2][0]

    def row_sum(self,arr,row_index):
        row_sum_value=0
        for i in range(3):
            row_sum_value+=arr[row_index][i]
        return row_sum_value

    def column_sum(self,arr,column_index):
        column_sum_value=0
        for i in range(3):
            column_sum_value+=arr[i][column_index]
        return column_sum_value
    
    def output_square(self):
        sample_list = [i for i in range(1,10)]
        perm_list = list(itertools.permutations(sample_list))
#          square_list=[]
        for perm in perm_list:
            new_square = []
            for i in range(0,9,3):
                new_square.append(perm[i:i+3])
            self.square_list.append(new_square)
        yes_magic=False
        for square in self.square_list:
            diagonal_sum = self.diag_sum(square)
            for i in range(3):
                if  (self.row_sum(square,i)==diagonal_sum and self.column_sum(square,i)==diagonal_sum and self.sec_diag_sum(square)==diagonal_sum):
                    yes_magic=True
                else:
                    yes_magic= False
                    break
            if yes_magic:
                self.magic_square_list.append(square)
        
        
# sample_list = [i for i in range(1,10)]
# perm_list = list(itertools.permutations(sample_list))
# square_list=[]
# for perm in perm_list:
#     new_square = []
#     for i in range(0,9,3):
#         new_square.append(perm[i:i+3])
#     square_list.append(new_square)
# # print(len(perm_list),len(square_list))
# def diag_sum(arr):
#     return arr[0][0]+arr[1][1]+arr[2][2]
# def sec_diag_sum(arr):
#     return arr[0][2]+arr[1][1]+arr[2][0]

# def row_sum(arr,row_index):
#     row_sum_value=0
#     for i in range(3):
#         row_sum_value+=arr[row_index][i]
#     return row_sum_value

# def column_sum(arr,column_index):
#     column_sum_value=0
#     for i in range(3):
#         column_sum_value+=arr[i][column_index]
#     return column_sum_value

# magic_square_list=[]
# yes_magic=False
# for square in square_list:
#     diagonal_sum = diag_sum(square)
#     for i in range(3):
#         if  (row_sum(square,i)==diagonal_sum and column_sum(square,i)==diagonal_sum and sec_diag_sum(square)==diagonal_sum):
#             yes_magic=True
#         else:
#             yes_magic= False
#             break
#     if yes_magic:
#         magic_square_list.append(square)

if __name__=="__main__":
    
    magic_square_object = GiveMagicSquare_3()
    magic_square_object.output_square()
    print(magic_square_object.magic_square_list)
    # magic_square = 


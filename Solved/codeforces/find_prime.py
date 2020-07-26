#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def find_prime_upto(n):
    prime_arr = [True for i in range(n)]
    prime_arr[0]=False
    for i in range(2,int(n**0.5)+1):
        if prime_arr[i-1]:
            for j in range(i**2,n+1,i):
                prime_arr[j-1]=False
    return [i+1 for i in range(n) if prime_arr[i]]


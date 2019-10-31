# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 08:38:45 2019

@author: Jama Hussein Mohamud
"""
 
def getunique(SET, n, x) : 
	unique = 0
	# Bit iteration
	for i in range(0, x) : 	
		# sum the bits 
		Sum = 0
		x = (1 << i) 
		for j in range(0, n) : 
			if (SET[j] & x) : 
				Sum = Sum + 1
		if (Sum % 3) : 
			unique = unique | x 
	return unique 
	
#%%
    
SET = [12, 1, 12, 3, 12, 1, 1, 2, 3, 2, 2, 3, 7] 

x = 32

n = len(SET) 

print("Unique Value " , getunique(SET, n, x)) 
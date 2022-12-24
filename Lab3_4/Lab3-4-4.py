# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 07:48:06 2021

@author: M
"""

"""
table[i][0][j]          i = 0, 1, 2
s[k]
startpoints[p]

"""

from operator import add
import numpy as np

def start(table,s):
    start = []          # List of start points
    
    for i in range(3):
        for j in range(4):
            if table[i][0][j] == s[0]:
                start.append([i,j])
                
    return start


def find_next(table, s, startpoints, last_change, memory) :
    
    if startpoints == []:
        return False
    else:
        if len(s) == 1:
            return True
        else:
            s = s[1:]
            change = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            next_startpoints = []
             
            for p in range(len(startpoints)):
    
                new_starts = start(table, s)
                
                for q in range(len(new_starts)):
                    for c in range(len(change)):
                        if list(map(add, startpoints[p], change[c])) == new_starts[q]:
                            if change[c] != list(np.array(last_change) * (-1)) or new_starts[q] != memory[max(-2, -1*len(memory))] :
                                next_startpoints.append(new_starts[q])
                                last_change = change[c]
                                memory.append(new_starts[q])
                                
                           
    
                            
            if next_startpoints == []:
                return False
            else:
                return find_next(table, s, next_startpoints, last_change, memory)
                

last_change = []
table = [["ABCE"],
         ["SFCS"],
         ["ADEE"]]

print("Enter a string:")
s = input()
startpoints =  start(table, s)
print(find_next(table, s, startpoints, last_change = [], memory = []))

    








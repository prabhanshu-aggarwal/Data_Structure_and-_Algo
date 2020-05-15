# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:51:57 2020

@author: Prabhanshu Aggarwal
"""

class Node():
    
    def __init__(self, data_value):
        self.data_value=data_value
        self.next_val = None
        
class LinkedList():
    
    def __init__(self):
        self.head = None
        
list1 = LinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thur")  

list1.head.next_val = e2
e2.next_val = e3
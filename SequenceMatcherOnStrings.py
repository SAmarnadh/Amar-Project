# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 19:54:15 2020

@author: Amarnadh
"""
from difflib import SequenceMatcher 
s1="abcd"
s2="ab"
seq=SequenceMatcher(a=s1,b=s2)
print("Using difflib")
print(seq.ratio()*100)


print()
import edit_distance
ref = "abdace"
hyp = "abdace"
sm = edit_distance.SequenceMatcher(ref,hyp)
print("Using edit_distance")
#print(sm.get_opcodes())
#print(sm.get_matching_blocks())
print("Ratio=",round(sm.ratio()*100,4))
print("Dist=",sm.distance())  # returns distance between two strings
print("Matchng=",sm.matches())  # returns no. of similar matches
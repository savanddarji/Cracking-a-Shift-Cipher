################### program for cracking shift cipher ########################
from __future__ import division
import numpy as np
import string
a = raw_input("Enter the cipher text: ").lower()
num = dict(zip(range(0,26),string.ascii_lowercase))# for reverse mapping: numbers to letter
def shift(l1,n1): # for left shift operation
    return l1[n1:] + l1[:n1]
a1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
W=[]
for charc in a1:
    b1 = a.count(charc)
    b1 = b1/26
    b1 = round(b1,7)
    W.append(b1)
A = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.0236,0.0015,0.01974,0.00074]
I =24
J=[]
t=0
while I>=0:
    B= shift(A,t)
    K = np.dot(W,B)
    K = round(K,6)
    J.append(K)
    I -= 1
    t+=1
#print J
L=max(J)#for highest number in the list
F = J.index(L)# retrieve the index of the maximum number
#F+=1
#print F
F=26-F
print '\n','Encryption key:',F
S1=[]
for character in a:
    number = ord(character) - 97
    number = ((number - F)%26)
    S1.append(number)
a1=[]
for i2 in S1:
    a1.append(num[i2])
print '\n','Your plain text:',''.join(str(elm) for elm in a1)

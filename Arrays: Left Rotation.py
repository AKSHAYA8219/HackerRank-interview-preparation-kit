#!/bin/python3

num=list(map(int,input().split()))
n=num[0]
d=num[1]
a=list(map(int,input().split()))
rot=d%n
new_a=[]
for i in range(0,n):
    new_a.append(a[(i+rot)%n])
for i in new_a:
    print(i,end=" ")

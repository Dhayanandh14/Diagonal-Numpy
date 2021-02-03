import random
import numpy
size=int(input("Enter Size: "))
lst=[]
lst2=[]
#this loop for appending the value into the list
for i in range(size*size):
    r=random.randint(1,5)
    lst.append(r)
print ("List:\n",lst)
print()

arr=numpy.array(lst).reshape(size,size)#changing list to array
print("Arrays:\n",arr)
print()

#this for first diagonal
i=0
j=0
while i<arr.shape[1]: 
    while j<=i:
       l=arr[i,j]
       j=j+1
    lst2.append(l)
    i=i+1

print("First Diagonal:",lst2)
print("First Diagonal sum is: ",sum(lst2))
print("First Diagonal Maximum is: ",max(lst2))
print("First Diagonal Minimum is: ",min(lst2))
print("First Diagonal Average is: ",sum(lst2)/len(arr))
print()

#This loop for second diagonal
k=arr.shape[1]-1 #column index
print(k)
m=0
c=0
lst3=[]
while k>=0:
    print(k)
    c=c+1
    while m<c:
       l1=arr[m,k]
       m=m+1
    lst3.append(l1)
    k=k-1

print ("Second Diagonal:",lst3)
print("Second Diagonal sum is: ",sum(lst3))
print("Second Diagonal Maximum is: ",max(lst3))
print("Second Diagonal Minimum is: ",min(lst3))
print("Second Diagonal Average is: ",sum(lst3)/len(arr))
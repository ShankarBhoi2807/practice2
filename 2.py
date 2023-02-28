'''print(list(range(4,20,2)))
print(sum([1,3,2,4],2))'''
#zip()
'''l1=["shankar","bapu","bhoi"]
l2=[1,2,3]
z=zip(l1,l2)
for l1,l2 in z:
    print("%s is %d"%(l1,l2))'''
#enumerate
'''list=["shankar","bapu","bhoi"]
for i,v in enumerate(list):
    print("%s:%s"%(i,v))'''

#min,max,sum,len,ascending,descending
'''L=[]
total_no=int(input("Total number of size is:"))
for e in range(total_no):
    n=int(input("enter a number:"))
    L.append(n)
print(L)
print("Minimum number of list is:",min(L))
print("Maximum number of list is:",max(L))
print("sum of number list is:",sum(L))
print("total length of list is:",len(L))
print("Ascending a number of list is:",sorted(L))
L.sort(reverse=True)
print("Descending a number of list is:",L)'''

#fibonacci series add to new list
'''n=int(input("enter a number:"))
a=0
b=1
c=0
list=[]
while c<=n:
    print(c)
    list.append(c)
    a=b
    b=c
    c=a+b
print("add a newlist is:",list)'''
number=int(input("Enter the Number: "))
a=0
b=1
for n in range(0,number):
           if n<=1:
               next=n
           else:
               next=a+b
               a=b
               b=next
           print(next)







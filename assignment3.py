#1

'''a=[1,2,3,4,5]
l=[]
l.append(a)
print(l)'''

#2

'''list=["google","apple","facebook","whatsapp"]
list.append(given)
print(list)'''

#3
'''l=[1,2,3,4,5,2]
l.count(2)
print(l.count(2))'''

#4

'''l=[19,2,7,4]
l.sort()
print(l)'''

#5
'''a=[1,4,6,7]
b=[2,5,8]
c=a+b
c.sort()
print(c)'''

#6
'''a=[1,2,3,4,5,6,7]
a.pop()
print(a)
a.append(9)
print (a)'''

#queue
'''import queue
a=queue.Queue(maxsize=20)
a.put(1)
a.put(2)
a.put(3)
a.put(4)
print(a.get())
print(a.get())
print(a.get())
print(a.get())'''


#optional question
l=[1,2,3,4,5,6,7]
odd=[]
even=[]
count=0
for x in l:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print("even list",even,len(even))
print("odd list",odd,len(odd))


import random
list1 = []
list2 = [] #Defined three list for 3x3 matrix.
list3 = []
pnumlis = [] #Defined pnumlist for prime numbers.

x = int(input("Base value of the range(x): "))
y = int(input("Top value of the range(y): "))

for i in range(x,y): #Program search for values between X and Y
    if i > 1:
        for n in range(2, i):
            if(i % n) == 0:
                break
            else:
                pnumlis.append(i) #Prime numbers between X and Y have been added to the list.

pnumlis = list(dict.fromkeys(pnumlis)) #Removed duplicated values from prime numbers list.
for j in pnumlis:
    random.shuffle(pnumlis) #Defined random.shuffle for unique values that comes from pnumlist.
    if len(list1) < 3:      #Program will ad maximum three values to lists.
        list1.append(j)
for k in pnumlis:
    random.shuffle(pnumlis)
    if len(list2) < 3:
        list2.append(k)
for m in pnumlis:
    random.shuffle(pnumlis)
    if len(list3) < 3:
        list3.append(m)

print("",list1,"\n",list2,"\n",list3)

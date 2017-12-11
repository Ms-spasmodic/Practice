import random
count = 0
while (count <  9 ):
    print ('The count is : ', count)
    count += 1
print ("Goodbye!")

print("Printing out X values")
for x in range(16):
    print(random.randint(1,10))
print("Printing out Y values")
for y in range(0,12,2):
    print(y)
print("Printing out Z vaules")
for z in range(10,-1,-1):
    print(z)

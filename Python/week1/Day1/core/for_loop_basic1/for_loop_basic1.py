for i in range(0,151):
    print(i)
for i in range(5, 1001, 5):
    print(i)
#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1, 101):
    if i % 5 == 0:
        print("Coding")
    elif i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)
# Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for i in range(1, 500001, 2):
    sum += i
print(sum)
#Print positive numbers starting at 2018, counting down by fours.
for i in range (2018, 0 , -4):
    print(i)
#Set three variables: lowNum, highNum, mult. Starting at lowNum 
#and going through highNum, print only the integers that are a multiple of mult. For example,
#if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum=2
highNum=9
mult=3
for i in range (2 , 10):
    if i%3==0:
        print(i)







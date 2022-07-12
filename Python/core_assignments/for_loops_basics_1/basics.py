# Print all integers from 0 to 150.
for x in range(0,151):
    print(x)

# Print all the multiples of 5 from 5 to 1,000
x=0
while x <= 1000:
    print(x)
    x = x+5

#Print integers 1 to 100. 
#If divisible by 5, print "Coding" instead. 
# If divisible by 10, print "Coding Dojo".

for x in range(0,101,1):
    if x%10==0:
        print('Coding Dojo')
    elif x%5==0:
        print('Coding')
    else:
        print(x)

#Print positive numbers starting at 2018, 
# counting down by fours.

for x in range(2018,0,-4):
    print(x)

#Set three variables: lowNum, highNum, mult. 
# Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum=2
highNum=9
mulNum=3
x = lowNum

while x <= highNum:
    if x%mulNum==0:
        print(x)
    x = x+1


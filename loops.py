#For loop to print even numbers
for i in range(1, 30):
    if (i%2 == 0):
        print(i)

#While loop to print even numbers
num = int(input(" Please Enter the Maximum number : "))
number = 1

while number <= num:
    if(number % 2 == 0):
        print("{0}".format(number))
    number = number + 1

#For loop to print odd numbers
for i in range(1, 30):
    if (i%2 != 0):
        print(i)   

#While loop to print odd numbers
num = int(input(" Please Enter the Maximum number : "))
number = 1

while number <= num:
    if(number % 2 != 0):
        print("{0}".format(number))
    number = number + 1
#Write a program to print your name 10 times
''
'''
name = "anjali kumari"
for i in range(10):
    print(name)
'''
# Write a program to print the series 1,2,3,4, ..,10.
''
'''
for i in range(1,11):
    print(i)
'''
#Write a program to print the series 2, 3, 4, .. ,20.
''
'''
for i in range(2,21):
    print(i)
'''
#Write a program to print the series 10, 9, 8, 7, ..,1
''
'''
for i in range(10,0,-1):
    print(i)
'''
#Write a program to print nos. divisible by 5 betwen 1-100
''
'''
for i in range(100):
    if i%5 == 0:
        print(i,end=" ")
'''
#Write a program to print nos. divisible by 2 and 3 both betwen 1-100.
''
'''
for i in range(100):
    if i%2 ==0 or i%5 == 0:
        print(i,end=" ")
'''
#Write a program to Find the Sum of Natural Numbers.
''
'''
num = int(input("enter a number"))
sum_digit = 0
temp = num
for i in range(1,num + 1):
    sum_digit += i
print(f"The sum of digit number is {sum_digit}")
'''
#Write a program to find sum of odd numbers between 1-100.
''
'''
total_sum = 0
for num in range(1,101,2):
    total_sum += num
print("The sum of odd numbers  between 1 and 100 is:",total_sum)
'''
# Write a program to print table of 2.
''
'''
for i in range(1,11):
    print("2*{i}:",{2*i})
'''
#Write a program to calculate factorial of a number using while loop.
''
'''
num = int(input("enter a number:"))
factorial = 1
temp = num
while temp > 0:
        fectorial = factorial * temp
        temp = temp - 1
print(f"The factorial of{num}is{factorial}")
'''
# Write a program to print average of 10 values entered by user.
''
'''
num = float(input("enter value {i+1}:"))
total_sum = 0
for i in range(10):
    total_sum += num
average = total_sum/10
print(f"the average of the 10 value  is:{average}")
'''
# Use a while loop to take inputs from the user and keep printing the square of the number.
''
'''
while True:
     num = float(input("enter a number (negative number to stop):"))
if num < 0:
    print("program stopped  because you entered a negative number.")
square = num**2
print(f"square of{num} is:{square}")
'''
# Input a number and reverse its digits using a while loop. Example: 1234 → 4321
''
'''
num =int(input("enter a number to reverse:"))
reverse_num = 0
temp = num
while temp > 0:
    digit = temp % 10
    reverse_num = (reversed_num*10)+ digit
    temp = temp//10
print(f"The reverse of{num} is:{reverse_num}")
'''

# asking for name and creating an empty list to fill in with the input of the user later. 

name = input("Enter your name? ")
list_1 = []

number_1 = int(input("Enter your first favorite number. "))
list_1.append(number_1)
number_2 = int(input("Enter your second favorite number. "))
list_1.append(number_2)
number_3 = int(input("Enter your third favorite number. "))
list_1.append(number_3)

print(list_1)

#Applying operations to check whether the input is an even or odd number.

print(f"Hello, {name.title()}!, Let's explore your favorite numbers.")

for number in list_1:
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else: 
        print(f"The number {number} is odd.")

#Applying for loop to put the three input numbers in a tuple and print their squares.
tuples = []

for number in list_1:
    tuple = (number, number **2)
    tuples.append(tuple)
print(tuples)

#Adding the input numbers and printing a message. 

sum_of_input = int(number_1 + number_2 + number_3)
print(f"And Voila, the sum of your favorite numbers is : {sum_of_input}")

#Determining if the sum of input is a prime number or composite number. 

if sum_of_input <= 1:
    print("And the sum of your favorite numbers is not a prime number.")
elif sum_of_input <= 3:
    print("And the sum of your favorite numbers is a prime number.")
elif sum_of_input % 2 == 0 or sum_of_input % 3 == 0 or sum_of_input % 5 == 0 or sum_of_input % (5 + 2) == 0: 
    print("And the sum of your favorite numbers is a composite number.")
else: 
    print("The sum of your favorite numbers is also a Prime Number!!! WOW")

 





          


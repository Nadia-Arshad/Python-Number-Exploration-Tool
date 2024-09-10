# ASSIGNMENT DETAILS:

## Part One:

In the first part of the code, I declared a variable "name" and used the input function to take the name of the user. 
Then I created an empty list, and in number_1, number_2 and number_3 variables got the integer values stored taken from the user. The user had to put in his/her three favorite numbers. 
In the end of the first part, the empty list will be filled with the user's input. I used the append method to fill the list.

## Part Two: 

In the second part of the code, I used the f-string to join both user's name and my text. We had to see if the numbers provided by the user are even or odd. I used the for loop for our list_1 and checked if we divide it by 2,  there is no remainder left. In case of no remainder, it will print "The number is even" (Used f-string here as well)Or else it will print that the number is odd. 

## Part Three: 

For the third part of the assignment, I created an empty tuple, used for loop on list_1 that will append the number and the square of the number to the tuple. 


**IMPORTANT NOTE**
<u>"I noticed that I cannot append a tuple but assigning it a square bracket turned the supposed tuple to a list. How could I use a for loop and then add elements to the tuple, as required in the assignment?"</u>

## Part Four:

In the following part, I created a variable named **sum_of_input** and used the add arithmetic operator to add all the three numbers provided by the user earlier. And then printed the sum of the number using f-string again.

## Part Five:

For the fifth and the final part, the most tricky one though. I used both for loop and if and else conditionals. First I set a boolean variable. Using if statement checked if **sum_of_input** is smaller than or equal to 1. Then  it is not a prime number. The boolean variable prime is set to *False*. This took out the possibility of all negative numbers to be prime as well. 

Moving forward, with for loop, I took all the numbers from **2** to the possible number we could get in **sum_of_input** - 1, and with if conditional, checked if sum_of_input is divisible by the numbers running in loop. If it's remainder is 0 then again it is not a prime number, hence prime boolean variable is set to *False* again.

**If prime** prints a message, "the number is prime" in case the above conditions are true, otherwise the **else** print statement runs, letting us know if the sum of numbers that the user gave us as his favorite numbers is a composite number. 

## THE END ... 
![Alt text](https://i0.wp.com/1000wordphilosophy.com/wp-content/uploads/2021/05/happiness.jpg?resize=656%2C300&ssl=1)

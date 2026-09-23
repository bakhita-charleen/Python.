#--------------------------------------------- Part A - for Loops -------------------------------------------------

#Q1. Use a for loop to print the numbers 1 to 10, one per line.
print("===== Loop numbers: 1-10 ===== ")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number) 

print()

#Alternative solution
print("=== Numbers: 1-10 ===")
for i in range (1, 11):
    print(i)

print()

#Q2. Loop over this list and print each item:  ['chapati', 'ugali', 'pilau', 'githeri', 'mandazi']
print("=== Meals === ")

meals =  ['chapati', 'ugali', 'pilau', 'githeri', 'mandazi']

for food in meals:
    print(food)
print()

#Q3. Use a for loop to print each character in the word 'Nairobi' on its own line.
print("===== Characters in Nairobi ===== ")

word = 'Nairobi'

for character in word:
    print(character)
print()

#Q4. Loop over a list of 5 prices and print each price with 'Ksh' in front:  [120, 250, 85, 320, 175]
print("==== Price in Ksh ====")

prices = [120, 250, 85, 320, 175]

for price in prices:
    print(f"Ksh. {price}")
print()

#Alternative solution
print("==== Prices ====")

prices = [120, 250, 85, 320, 175]

for price in prices:
    print("Ksh.",price)
print()

#Q5.  Given this list of temperatures: [22, 35, 18, 40, 29, 15, 33], use a for loop to print only temperatures above 30. 
#  (Hint: use an if inside the loop)
print("==== Temperature ==== ")
temperatures = [22, 35, 18, 40, 29, 15, 33]

for temperature in temperatures:
    if temperature > 30:
        print(temperature)
print()

# ----------------------------------------------- Part B  range() ----------------------------------------------------

#Q6. Print all odd numbers from 1 to 19 using range().  (Hint: range(1, 20, 2))
print("=== Odd numbers ===")

for i in range (1, 20, 2):
    print(i)
print()

#Q7. Print the 8 times table from 8×1 to 8×12 using range().
print("=== Multiplication table for 8 ===")

for i in range (1, 13):
    result = 8 * i
    print(f"8 * {i} = {result}")
print()

#Q8. Use range() to print a countdown from 10 to 1, then print 'Happy New Year!'
print("=== Countdown === ")

for i in range (10, 0, -1):
    print(i)
print("Happy New Year")
print()
    
#Q9. Use range() and a loop to calculate 5! (5 factorial = 5 × 4 × 3 × 2 × 1). 
# (Hint: start result = 1,multiply each time)
print("===== 5 factorial ===== ")

result = 1

for i in range (1, 6):
    result = result * i
print(f"5!= {result}")
print()

#Q10. Use a for loop and range() to calculate the sum of all numbers from 1 to 1000. Print the result.
print(" === Sum of numbers === ")
result = 0

for i in range (1, 1001):
    result = result + i
print(f"Sum = {result}")
print()

# -------------------------------------- Part C : while Loops --------------------------------------------------

#Q11. Write a while loop that counts from 1 to 10 and prints each number.
print("===== While loop printing all numbers ===== ")

number = 1
while number <= 10:
    print(number) 
    number += 1

#Q12. Ask the user to keep entering numbers until they type 0. When they type 0, print the total of all numbers entered. 
#  (Hint: use while True and break)
print("===== While True and break ===== ")

num = 0

while True: 
    entry = int(input(" Enter number (or 0 to stop): "))
    if entry == 0:
        break
    num += entry
print(f"Total is: {num}")

#Q13. Write a password checker: keep asking for the password until the user gets it right. 
# The correct password is 'kenya2024'. Count and display how many attempts it took.
print("===== Password Checker =====")

correct_password = "kenya2024"
attempts = 0

while True:
    entry = input("Enter password: ")
    attempts += 1

    if entry == correct_password:
        break
    print("Incorrect password. Try again.")
print("Correct password!")
print("Attempts =", attempts)


#Q14.  A data pipeline processes records one at a time. Simulate this: start with records_remaining = 50. 
# Each loop reduces it by a random number between 5 and 15. Print progress each round until 0 or below.  
# (Hint: use import random and random.randint(5,15))

import random
 
print("=" * 40)
print("REMAINING RECORDS")
print("=" * 40)
 
records_remaining = 50
 
while True:
    records_remaining -= min(random.randint(5,15), records_remaining)
    print(f"There are {records_remaining} records remaining")
    if records_remaining <= 0:
        break
 
print("=" * 40)
print("THERE ARE NO RECORDS REMAINING")
print("=" * 40)

import random
 
records_remaining = 50
round_num = 1
 
while records_remaining > 0:
    processed = random.randint(5,15)
    records_remaining -= processed
    print(f"Round {round_num}: processed {processed} records, {max(records_remaining,0)} records remaining")
    round_num += 1
print("All records processed")


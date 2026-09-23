# Example 3 : Doing calculations inside a loop

#Multiplication table for the number 7
for i in range(1, 11):
    result = 7 * i
    print(f"7 * {i} = {result}")

#accumulating
#Add Mpesa transactions

transactions = [1500, 3000, 800, 12000, 450, 2700]

total = 0 #start at zero BEFORE the loop

for amount in transactions:
    total = total + amount #add each amount to running total
    print(f"Added Ksh {amount} Running total: Ksh {total} ")

print(f"Final total: Ksh {total}")

 #Loop 1: Print the numbers 1 to 10, each on its own line
print("Loop 1: numbers 1-10")

for i in range(1,11):
    print(i)
    print()

#Loop 2: Loop over this list and print each city: ['Nairobi','Mombasa','Kisumu','Nakuru','Eldoret']

print("--------- Cities ---------")
cities = ['Nairobi','Mombasa','Kisumu','Nakuru','Eldoret']

for city in cities:
    print(city)
    print()

#Loop 3: Loop over this list of prices: [250, 980, 120, 1500, 75]
#Print each price AND whether it is 'Affordable' (below 500) or 'Expensive' (500+)
#For Loop 3, you need an if/else INSIDE your for loop - that is perfectly fine.

prices = [250, 980, 120, 1500, 75]

for pricing in prices:
    if pricing < 500 :
        status = 'Affordable'
    else : status = 'Expensive' 

    print(f"Ksh {pricing} - {status}")
    print()
#Create a list of 5 student scores: [78, 85, 91, 65, 72]
#Use a for loop to calculate: total, count of students above 70, and the average
#Print all three results after the loop
#Remember: total = 0 and above_70 = 0 BEFORE the loop.
#Expected: Total=391, Above 70=4, Average=78.2

#list of scores
scores = [78, 85, 91, 65, 72]

#Initialize accumulators before the loop
total= 0
above_70 = 0

for score in scores:
    total = total + score  # total += score
    if score > 70:
        above_70 = above_70 + 1

#Calculate average = Total/no of score (len(scores))
# Total divided by the number of scores
average = total / len(scores)

#Print all three results after the loop
print(" === Student Scores Report === ")
print(f"Total: {total}")
print(f"Above 70: {above_70}")
print(f"Average: {average}")
print()
    
# =====================================
# While loop
# =====================================

#eXAMPLE - While loop with user input

print("========== While loop with user input ==========")
score = -1

while score < 0 or score > 100:
    score = int(input("Enter score (0-100):"))
    if score < 0 or score > 100:
        print("Invalid! Score must be between 0 and 100")

print(f"Valid score accepted: {score}")
print()

# While_break example
print("======= While_break ======= ")

while True:
    entry = input("Enter amount (or done to finish): ")

    if entry.lower() == "done":
        break #exit the loop immediately
    amount = int(entry)
    total += amount    #total = total + amount
    print(f"Running total: Ksh {total}")
print(f"Final total: Ksh {total}") 
print()

#Program 1: Countdown
#Ask: 'Start countdown from: ' (int)
#Use a while loop to count DOWN to 1, printing each number
#After the loop print: 'Blast off! '

print(" ========= Countdown =======")
start = int(input("Start countdown from: "))
while start >= 1:
    print(start)
    start -= 1

print("Blast off!")
print()

#Savings goal calculator
#Ask: 'What is your savings goal (Ksh)? ' (int)
#Ask: 'How much can you save per month (Ksh)? ' (int)
#Use a while loop: each round add monthly savings, print running total
#Stop when total reaches the goal. Print how many months it took.
#Test Program 2 with: goal=50000, monthly=8000
#Expected: 7 months to reach Ksh 56,000

print("============ Savings goal calculator ===============")
#Ask for savings goal + monthly saving
goal = int(input("What is your savings goal (Ksh)? "))
monthly = int(input("How much can you save per month (Ksh)? "))

# Initialize variables
total = 0
months = 0

while total < goal:
    total += monthly
    months += 1
    print("Month", months, ":", "Ksh", total)

print(months, "months to reach Ksh", total) 

#Infinite loop
password = " "
while password != 'python123':
    print("wrong password!")
    password = input("Enter password: ")
print("Access granted")

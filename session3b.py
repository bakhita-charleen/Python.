#Infinite loop

password = " "
while password != 'python123':
    print("wrong password!")
    password = input("Enter password: ")
print("Access granted")


while True:
    name = input("Enter your name(or type quit): ")

    if name == 'quit':
        break
    print(f"Hello, {name}")

# ------------------- Break and Continue --------------------------------

# Example: Break - Stop the loop early

# Find the first score below 40 and stop
scores = [78, 85, 91, 35, 66, 55, 42]

for score in scores:
    if score < 40:
        print(f"First failing score found: {score}")
        break
    print(f" {score} --> OK")

print("Search complete")

# 66, 55 and 42 are never checked. Break stopped the loop after getting 35.
# The code after the loop ("Search complete") still runs - break only exits the loop

# ===== Example 9: Break and continue side by side

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using BREAK - stop at 5
print ("With break")
for num in numbers:
    if num == 5:
        break
    print(num, end=" ")
print()

# Using continue
print ("With continue")
for num in numbers:
    if num == 5:
        continue
    print(num, end=" ")
print()

# Print only valid scores - skip anything that is -1(absent)
print()
print("Present Student Scores")
scores = [78, -1, 85, -1, 91, 65, -1, 72]

names = ["Alicia", "Brian", "Bob", "Otieno", "Wanjiku", "Kamau", "Aisha", "Mwangi"]

for i in range(len(scores)):  #range(8) 0,1,2,...........7
    if scores[i] == -1:
        continue #Skip absent students
    print(f"  {names[i]}: {scores[i]}")


#List: transactions = [500, 1200, -200, 8500, 15000, -500, 3000]
# Loop 1 (using continue): Print only POSITIVE transactions. Skip negative ones with continue. Print the total of positive transactions.
# Loop 2 (using break): Loop through transactions.    If any transaction is above 10000, print 'Large transaction flagged: Ksh X' and STOP.    Otherwise print 'Ksh X — OK'
# Expected Loop 1: 500, 1200, 8500, 15000, 3000 — Total: Ksh 28,700 Expected Loop 2: 500 OK, 1200 OK, -200 OK, 8500 OK, FLAGGED 15000


# ========== Example =================

# Transactions list
transactions = [500, 1200, -200, 8500, 15000, -500, 3000]

# Loop 1: Using continue
print("===== Loop 1: Positive Transactions ===== ")

total = 0

for transaction in transactions:
    if transaction < 0:
        continue
    print(f"Ksh {transaction}")
    total += transaction
print(f"Total: Ksh {total}")
print()

# Loop 2: Using break
print("===== Loop 2: Transaction Check ===== ")

for transaction in transactions:
    if transaction > 10000:
        print(f"Large transaction flagged: Ksh {transaction}")
        break
    print(f"Ksh {transaction} — Ok")
print()

# ============ Example 11 - Enumerate ==============

students = ["Bob", "John", "Njeri", "Wanjiku"]

# Without enumerate
for i in range(len(students)):
    print(f"{i + 1}. {students[i]}" )
print()

# With enumerate
for pos, student in enumerate(students, start=1):
    print(f"{pos}.  {student}")

    students = ["Bob", "John", "Njeri", "Wanjiku"]
print()

# =============== Example 12 - Enumerate: If statement ===================
scores = [78, 85,45, 91, 38, 65, 72]
#Student 1: 78 PASS
print("Students Result Score")
print("-" * 30)
for position, score in enumerate(scores, start=1):
    if score < 50:
        status = "FAIL"
    else:
        status = "PASS"
    print(f"    Student {position}: {score} {status}")
print("-" * 30)
print(f"Total students: {len(scores)}") 
print()

# Task 1: Print a numbered menu    items = ['Check balance','Send money','Buy airtime','Withdraw','Exit']   
#  Use enumerate(start=1) to print:    1. Check balance    2. Send money   ...etc
print("---------- Menu items ----------")
menus = ['Check balance','Send money','Buy airtime','Withdraw','Exit'] 

for pos, menu in enumerate(menus, start=1):
    print(f"{pos}. {menu}")
print()

# Task 2: Numbered exam paper with question numbers questions = ['What is a variable?','What does print() do?',   
# 'Name two data types','What is a loop?','What is if/else?']    
# Print each as: Q1. What is a variable?  Q2. What does print() do? ...etc  
#   Then print 'Total questions: 5' after the loop

print("---------- Numbered exam paper ----------")
total = 0

questions = ['What is a variable?',
             'What does print() do?',   
             'Name two data types',
             'What is a loop?',
             'What is if/else?'] 

for  pos, question in enumerate(questions, start=1):
    print(f"Q{pos}. {question}")
print(f"Total questions:", len(questions))
print()

# ================ Example 13: Basic nested loop ===============
days = ["Monday", "Tuesday", "Wednesday"]
periods = ["period 1", "period 2", "period 3"]

for day in days:
    print(f"--- {day} ---")
    for period in periods:
        print(f"    {period}")
    print()

# ================ Example 14:  ========================

# Maths       English     Science
# 0               1           2
# 78              85          90  0   Bob
# 65              72          68  1   John
# 91              88          95  2   Njeri

#---- Bob --------
# Maths: 78
# English: 85
# Science: 90
# Average: 84.3

students = ["Bob", "John", "Njeri"] 
subjects = ["Maths", "English", "Science"]

scores = [
    [78, 85, 90], # Bob's score
    [65, 72, 68], # John's score
    [91, 88, 95] # Njeri's score
]

# print(scores[0][2]) #index for the row, then index for the column

for i, student in enumerate(students):
    print(f"--- {student} ---")
    total = 0
    for j, subject in enumerate(subjects):
        score = scores[i][j]
        total += score
        #1st round - i = 0, j = 0
        #2nd round - i =0, j = 1
        #3rd round - i =0, j=2
        print(f"     {subject}: {score}")
    average = total / len(subjects)
    print(f"     Average: {average:.1f}") 
    print()
# ===================== Example 1: Local variables stay local =========================

def calculate_fee():
    fee = 5000          #LOCAL - only exists inside this function
    print(f"Fee inside function: {fee}")

calculate_fee()
#print(fee) # NameError! fee does not exist out here
#the local variable fee is gone after the function finishes.

# ======================= Example 2: Reading global variable ========================
school = "Nairobi Tech Institute"   #GLOBAL Variable

def show_school():
    # can READ global variables
    print(f"School: {school}")

show_school()
print(f"Also here: {school}")       #global accessible everywhere


# =================== Example 2: ==========================

city = "Nairobi"        #GLOBAL city
def show_local():
    city = "Mombasa"        #LOCAL city - a DIFFERENT variable , same name
    print(f"Inside function: {city}")

show_local()
print(f"Outside the function: {city}")


# Example 3: Global keyword (only when you MUST change a global)

login_count = 0         # global counter

def login(username):
    global login_count  # tell python: use the GLOBAL login_count
    login_count += 1
    print(f"{username} logged in. Total logins: {login_count}")

login("Navas")
login("Peter")
login("Nelly")
login("Bob")
print(f"Final count: {login_count}") 
print()

# Create global variable  total_sales = 0
#    Write a function add_sale(amount) that adds amount to total_sales (use global keyword)
#    Call add_sale three times with different amounts
#    Print total_sales after all three calls
#    Expected: total_sales should be the sum of all three amounts

total_sales = 0

def add_sale(amount):
    global total_sales
    total_sales += amount

add_sale(700)
add_sale(7000)
add_sale(70000)
print(f"Total sales: {total_sales}")
print()

# ================= Example 4: Basic *args ========================

def total_cost(*prices):
    print(f"Prices received: {prices}")
    return sum(prices)

#call with any number of arguments
print(total_cost(150))
print(total_cost(150,70,700))
print(total_cost(77, 770, 7700, 7770, 7777))
print()


# ========== Example 4: *args with required parameter before it

# Regular parameters come BEFORE *args
def class_summary(teacher, *scores):
    print(f"Teacher: {teacher}")
    print(f"Students: {len(scores)}")
    if scores:
        print(f"Average: {sum(scores)/len(scores)}")
        print(f"Highest: {max(scores)}")
    print()

class_summary("Mr.Gidi", 78, 85, 91, 65, 72)
class_summary("Ms.Wanjiku", 88,94,76)

"""
Results for 100m sprint
1. Otieno
2. Kiptoo
3. Mwangi
"""

def announce_winners(event, *names):
    print(f"Results for {event}")
    for i, name in enumerate(names, start =1):
        print(f" {i}. {name}")

announce_winners("100m Sprint", "Otieno", "Kiptoo", "Mwangi")
print()

# data_pipeline(name, *steps) — prints a pipeline with numbered steps
#    Test: data_pipeline('Sales ETL', 'Extract CSV', 'Clean data', 'Load to DB')
#    Expected output:
#    Pipeline: Sales ETL
#    Step 1: Extract CSV
#    Step 2: Clean data
#    Step 3: Load to DB

def data_pipeline(name, *steps):
    print(f" Pipeline: {name}")
    for i, step in enumerate(steps, start=1):
        print(f" Step {i}: {step}")

data_pipeline("Sales ETL", "Extract CSV", "Clean data", "Load to DB") 
print()
# multiply_all(*numbers) — returns the product of all numbers
#    Test: multiply_all(2, 3) → 6
#          multiply_all(1, 2, 3, 4, 5) → 120
#    Hint: start result=1, loop through and multiply

def multiply_all(*numbers):
    result = 1
    
    for number in numbers:
        result = result * number
    return result

print(multiply_all(2, 3))
print(multiply_all(1, 2, 3, 4, 5))






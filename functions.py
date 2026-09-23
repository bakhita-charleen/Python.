# ========================================
# Without functions
# =========================================

#Calculating VAT for 3 items - without a function
# same code repeated 3 times

# =============== With a Function ===================

def add_vat(price, rate=0.16):
    vat = price * rate
    total = price + vat
    return total

print(add_vat(1000))
print(add_vat(2500))
print(add_vat(750))

# ------------------- Define function --------------------------

def print_divider():
    print("=" * 40)

print_divider()
print(" STUDENT REPORT")
print_divider
print(" Amina: 87 ")
print(" Moses: 74 ")
print_divider()


# ----------------- Define function, function with one parameter ------------------------------

def greet(name):
    print(f"Good morning, {name}! Welcome to Python class.")

greet("Bob")
greet("Mercy")
print()

# ------------------- Define function, function with multiple parameters ----------------------------------

def student_info(name, age, track):
    print(f"Name:   {name}")
    print(f"Age:    {age}")
    print(f"Track:  {track}")
    print()

student_info("Brian", 22, "Data Engineering")
student_info("Alice", 20, "Data Science")
student_info(age=25, track="Data Engineering", name="Moses")

# Describe student, parameters = name, city, track
#Bob is from Nairobi studying Data Science

def describe_student(name, city, track):
    print(f"{name} is from {city} studying {track}")

describe_student("Bob", "Nairobi", "Data Science")


# Write a function called get_grade , returns a letter grade based on this scale
# 80 and above - A
# 70 - 79      - B
# 60 - 69      - C
# 50 - 59      - D
# Below 50     - F
 
# use function to print the grade of these students
# Amina: 78
# Brian: 65
# Peter : 91
 
# Amina: 78 --> Grade B

def get_grade(name, score):
    grade =""
    if score > 80:
        grade = "A"
    elif score > 70:
        grade = "B"
    elif score > 60:
        grade = "C"
    elif score > 50:
        grade = "D"
    else:
        grade = "F"
   
    return(f" {name} --> {score}:  Grade {grade}")
 
print(get_grade("Amina", 78))
print(get_grade("Brian", 65))
print(get_grade("Peter", 91))

def grade(name, score):
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
       
    print(f"{name} --> {grade}")

grade("Amina", 78)
grade("Brian", 65)  
grade("Peter", 91)

def letter_grade(score, name):
    score = int(input("Enter the score"))
    if score >= 80:
        print(f"{name}: {score} --> Grade A")
    elif 70 <= score <= 79:
        print(f"{name}: {score} --> Grade B")
    elif 60 <= score <= 69:
            print(f"{name}: {score} --> Grade C")
    elif 50 <= score <= 69:
            print(f"{name}: {score} --> Grade D")
    elif 50 < score:
            print(f"{name}: {score} --> Grade F")
    else:
          print("invalid score")
       
letter_grade(name= "Amina", score=78)
 
def get_grade(score):
    if score >= 80:
        return  "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def print_all_grades(*students):
    for name, score in students:
        print(f"{name}: {score} --> Grade {get_grade(score)}")


print_all_grades(("Amina", 78), ("Brian", 65), ("Peter",91), ("Bob", 20))
 
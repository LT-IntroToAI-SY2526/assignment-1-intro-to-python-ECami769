# Assignment 1: AI-Generated Python Problems
# Name: Elisabeth Cami

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
"I'm learning Python basics in a high school programming class and I'm new to programming. 
Can you create 5-7 practice problems that cover Variables and basic data types Conditionals (if/elif/else) 
Loops (for and while) Functions Basic list operations"

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: Variables and Basic Data Types
Create a program that asks the user for their name and age. Then print a message saying:
Hello, [name]! You are [age] years old.
"""
# name = input("What is your name? ")
# age = input("How old are you? ")

# print("Hello,", name + "! You are", age, "years old.")
"""
Example:

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""
"""
PROBLEM 2: Conditionals (if/elif/else)
Ask the user to enter the temperature (in Celsius). Then print a message depending on the temperature:
Below 0°C → "It's freezing!"

0-20°C → "It's cold."

21-30°C → "Nice weather."

Above 30°C → "It's hot!"









# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================



Test- all your solutions with different inputs

Add asserts: if you feel comfortable

# Example:"""
# print("Testing Problem 1:")
# print(f"is_even(4): {is_even(4)}")  # Should print True
# print(f"is_even(7): {is_even(7)}")  # Should print False



print("Testing Problem 1:")
name = input("What is your name? ") #Ask the user for input
age = input("How old are you? ") #This is a string by default
age = int(age)
print("In 5 years you will be", age + 5)

print("Testing Problem 2:")

num = int(input("What is the tempeature?"))
if num <= 20:
    print ("It's cold!")
elif 20 < num < 30:
    print ("Nice weather.")
else:
    print ("It's hot!")


print("\nTesting Problem 3:")
times = int(input("How many nights do you want to log?"))
for i in range(times):
    print(int(input("How many stars did you see?")))

print("\nTesting Problem 4:")
def greet_all(names):
    for name in names:
        print("Hello,", name + "!")

names = ["Ava", "Matt", "Jane", "Kate"]
greet_all(names)

print("\nTesting Problem 5:")
favorite_food = input("What is your favorite food?")
print("Sounds good!")

favorite_color = input("What is your favorite color? Blue, red or green?")
if favorite_color == "blue":
    print("Like the sky!")
elif favorite_color == "red":
    print("Reminds me of strawberries.")
elif favorite_color == "green":
    print("Like the nature.")
else:
    print("That's also a good choice!")



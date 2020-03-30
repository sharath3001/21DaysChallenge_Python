# odd even counter
odd_numbers = 0
even_numbers = 0
number = int(input("Enter a number or type 0 to stop: "))
while number != 0:
    if number % 2 == 1:
        odd_numbers += 1
    else:
        even_numbers += 1
    number = int(input("Enter a number or type 0 to stop: "))
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

# magician number guessing
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input())

while number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    number = int(input("Enter another number: "))
print("Well done, muggle! You are free now.")

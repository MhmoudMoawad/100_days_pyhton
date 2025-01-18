import random

# Create an empty list
random_list = []

# Generate 100 random numbers and append them to the list
for _ in range(100):
    random_number = random.randint(1, 100)  # Generates numbers between 1 and 100 (inclusive)
    random_list.append(random_number)

print(random_list)
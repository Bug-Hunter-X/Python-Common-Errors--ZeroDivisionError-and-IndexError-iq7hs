def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    return sum(numbers) / len(numbers)

# Example usage with error handling:
my_numbers = []
average = calculate_average(my_numbers)
print(f"Average: {average}")

my_numbers = [10, 20, 30]
average = calculate_average(my_numbers)
print(f"Average: {average}")

#Handling potential IndexError
my_list = [1,2,3,4,5]

try:
    print(my_list[10])
except IndexError:
    print("Index out of bounds")

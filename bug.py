def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage (potential for ZeroDivisionError):
my_numbers = []
average = calculate_average(my_numbers)
print(f"Average: {average}")

#Another example with a potential IndexError
my_list = [1,2,3,4,5]
print(my_list[10])

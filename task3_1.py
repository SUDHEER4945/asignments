#Given list of numbers
numbers = [5, 12, 3, 8, 21, 10, 15, 6, 18]

#the sum of all even numbers
even_sum = sum(num for num in numbers if num % 2 == 0)
print("Sum of even numbers:", even_sum)

#maximum value
max_value = max(numbers)
print("Maximum value:", max_value)

# Create list with numbers greater than 10
greater_than_10 = [num for num in numbers if num > 10]
print("Numbers greater than 10:", greater_than_10)
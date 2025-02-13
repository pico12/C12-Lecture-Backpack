def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            numbers.append(num)
    return even_numbers

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def find_max(numbers):
    max_num = 0
    for num in numbers:
        if max_num < num:
            max_num = num
    return max_num

# Main function
def main():
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(num) for num in user_input.split()]
    
    even_numbers = filter_even_numbers(numbers)
    print(f"Even numbers: {even_numbers}")
    
    even_sum = calculate_sum(even_numbers)
    print(f"Sum of even numbers: {even_sum}")
    
    max_number = find_max(numbers)
    print(f"Maximum number: {max_number}")

main()

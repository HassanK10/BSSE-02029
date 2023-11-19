

for i in range(1, 11):
    current_number = i
    previous_number = i - 1 if i > 1 else 0
    sum_of_numbers = current_number + previous_number
    print(f"Current number {i}: previous number {previous_number} Sum is {sum_of_numbers}")
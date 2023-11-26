
def check_number(numbers):
    if numbers:
        return numbers[0] == numbers[-1]
    else:
        return 0

my_list = [3, 1, 8, 3, 9, 3]

result = check_number(my_list)
print("the first and last numbers are same or not ? :", result)
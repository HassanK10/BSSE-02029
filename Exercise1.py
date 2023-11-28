

def calculate_result(n1, n2):
    product = n1 * n2
    if product <= 1000:
        return product
    else:
        return n1 + n2
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second inte ger: "))
result = calculate_result(num1, num2)
print("Result is:", result)
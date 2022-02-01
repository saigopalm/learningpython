# Program to convert an integer in decimal to binary form

# function to convert decimal to bianry
def convert(num1):
    binary = str('')
    while(num1 > 0):
        binary = str(num1 % 2) + binary
        num1 = num1 // 2
    return binary


print('Enter a number in decimal form')

num = int(input())

bin = convert(num)      # calling the convert function

print('The number you entered in binary form is ' + bin)


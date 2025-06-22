#5. Factorial calculator

while True:
    try: 
        factorial_input = int(input("please enter any number."))
        if factorial_input == 0:
            print(1)
            break
        elif factorial_input < 0:
            print("nonegative numbers do not have a definitive factorial. please enter a number zero and above.")
        else:
            break
    except ValueError:
        print("not a valid input. must be an int zero and above")

count = factorial_input
multiple = 1
while count > 0:
    multiple *= count
    count -= 1

print(f"{factorial_input} factorial is: {multiple}.")

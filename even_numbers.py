#4. Print even numbers up to N

while True:
    try:
        number_input = int(input("please enter any number"))
        break
    except ValueError:
        print("you must input a number")

count = 2
print("here is a list of even numbers greater than zero, preceding the number you inputted:")
while count <= number_input:
    print(count)
    count += 2

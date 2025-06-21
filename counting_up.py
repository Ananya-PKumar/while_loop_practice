#1.Counting up to a number

while True:
    try:
        number = int(input("please enter any number"))
        break
    except ValueError:
        print("please only enter a number")

count = 1
while count <= number:
    print(count)
    count += 1

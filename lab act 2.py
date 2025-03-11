def check_numbers(num):
    if num % 2 == 0:
        print(f"{num} is an Even number.")
    else:
        print(f"{num} is an Odd number.")



num = int(input("Enter a number mo pare: "))
check_numbers(num)
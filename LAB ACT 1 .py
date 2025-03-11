def classify_age(age):
    if age < 0:
        print("Invalid age. Please enter a non-negative number. yung totoo lang pp")
    elif age <= 12:
        print("You are a Child. (bata ka pa)")
    elif age <= 19:
        print("You are a Teen.(pwede na)")
    elif age <= 64:
        print("You are an Adult(matanda na)")
    else:
        print("You are a Senior citizen.")

12

age = int(input("Enter your age: "))
classify_age(age) 
num = int(input("Enter a number: "))
if num % 11 == 0 and num % 5 == 0:
    print("Divisible by both 11 and 5")
elif num % 11 == 0:
    print("Divisible by 11")
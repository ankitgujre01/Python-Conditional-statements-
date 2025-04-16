'''
1. percentage is greater than 75 or equal print dist.
2. percentage is greater than equal to 60 or less than 75 1st div
3. percentage is greater than equal to 50 or less than 60 2nd div
4. percentage is greater than equal to 35 or less than 50 2nd div
5. percentage is less than 35 fail
'''
percentage = float(input("Enter percentage: "))

if percentage>=75:
    print("Dis")
elif percentage>=60 and percentage<75:
    print("1st division")
elif percentage >= 50 and percentage<60:
    print("2nd division")
elif percentage >= 35 and percentage<50:
    print("3rd division")
else:
    print("fail")
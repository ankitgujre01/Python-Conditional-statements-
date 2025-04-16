''''
///////////Blood Donate//////////////
1. age>=18
2. wheight >=50
3. if weight and age are match then user can donate the blood
4. if age is less than 18 show under age
5. if weight is less than 50 show message under weight
6. if age is does not match than it should not ask weight
'''
age = int(input("Enter Your Age: "))

if age>=18:
    weight = float(input("Enter your weight: "))
    if weight >=50:
        print("please donate blood")
    else:
        print("under weight")
else:
    print("under age")
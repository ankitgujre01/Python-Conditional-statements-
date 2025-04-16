Age_Chunnu = int(input("Enter Your Age of Chunnu: "))
Age_Raju = int(input("Enter Your Age of Raju: "))
Age_Sam = int(input("Enter Your Age of Sam: "))

if Age_Chunnu < Age_Raju and Age_Chunnu < Age_Sam:
    print("Chunnu is Youngest")
elif Age_Raju < Age_Chunnu and Age_Raju < Age_Sam:
    print("Raju is Youngest")
elif Age_Sam < Age_Chunnu and Age_Sam < Age_Raju:
    print("Sam is Youngest")
else:
    print("All are same age")    
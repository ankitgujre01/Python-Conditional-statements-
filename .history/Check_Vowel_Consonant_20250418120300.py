character = input("Enter a character: ")
if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
    print(character, "is a vowel")
elif character == 'A' or character == 'E' or character == 'I' or character == 'O' or character == 'U':
    print(character, "is a vowel")
elif character >= 'a' and character <= 'z' or character >= 'A' and character <= 'Z':
    
else:
    print(character, "is a consonant")
character = input("Enter a character: ")
if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
    print(character, "is a vowel")
elif character == 'A' or character == 'E' or character == 'I' or character == 'O' or character == 'U':
    print(character, "is a vowel")
elif character == "~, `, !, @, #, $, %, ^, &, *, (, ), -, _, +, =, {, }, [, ], |, \, :, ;, ', \", <, >, ,, ., ?, /":
    print(character, "is a special character")
elif character.isdigit():
    print(character, "is a digit")
else:
    print(character, "is a consonant")
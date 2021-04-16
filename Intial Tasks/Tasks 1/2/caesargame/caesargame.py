def encrypt(string, shift_key,option):
    cipher_text = ''

    if(option==1):
        for char in string:
            if char == ' ':
                cipher_text = cipher_text + char
            elif char.isupper():
                cipher_text = cipher_text + chr((ord(char) - shift_key - 65) % 26 + 65)
            elif char.islower():
                cipher_text = cipher_text + chr((ord(char) - shift_key - 97) % 26 + 97)
            else:
                cipher_text = cipher_text + char

    if (option == 0):
        for char in string:
            if char == ' ':
                cipher_text = cipher_text + char
            elif char.isupper():
                cipher_text = cipher_text + chr((ord(char) + shift_key - 65) % 26 + 65)
            elif char.islower():
                cipher_text = cipher_text + chr((ord(char) + shift_key - 97) % 26 + 97)
            else:
                cipher_text = cipher_text + char

    return cipher_text

number_chosen = int(input())
option= int(input())
string_input = input()
temp=encrypt(string_input, number_chosen,option)
print(temp.lower())
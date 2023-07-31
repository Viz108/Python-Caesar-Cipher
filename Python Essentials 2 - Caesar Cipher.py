
orig_text = input("Enter a string to encrypt: ")
shift = int(input("Enter number of characters to shift: "))
encrypted_text = ""

for char in orig_text:
    if not char.isalpha():
        encrypted_text += char
        continue
    else:
        char_code = ord(char) + shift
        if char.islower():
            if char_code > ord('z'):
                char_code = (ord('a') - 1) + (char_code - ord('z'))
        elif char.isupper():
            if char_code > ord('Z'):
                char_code = (ord('A') - 1) + (char_code - ord('Z')) 
        encrypted_text += chr(char_code)

print(encrypted_text)
        

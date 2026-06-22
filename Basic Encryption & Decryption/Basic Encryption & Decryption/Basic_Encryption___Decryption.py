#char = input("Enter a character: ")
#Shift = int(input("Enter the shift value: "))
#Encryted = chr(ord(char) + Shift)
#print ("Encrypted character: ", Encryted)
print ("================== Welcome to Encrypted & Decrypted App ==================")
Text = input("Enter a text: ")
Shift = int(input("Enter the shift value: "))
Encrypted_text = ""
Decrypted_text = ""

for n in range(len(Text)):
    char = Text[n]
    if (ord(char) >= 65 and ord (char) <= 90):
        Encrypted_char = chr((ord(char) - 65 + Shift)%26 + 65)
        Encrypted_text += Encrypted_char
    
    elif (ord(char) >= 97 and ord (char) <= 122):
        Encrypted_char = chr((ord(char) - 97 + Shift)%26 + 97)
        Encrypted_text += Encrypted_char
    
    else:
        Encrypted_text += char
    
print ("Encrypted text is: " , Encrypted_text)

for n in range(len(Encrypted_text)):
    char = Encrypted_text[n]
    if (ord(char) >= 65 and ord (char) <= 90):
        Decrypted_char = chr((ord(char) - 65 - Shift)%26 + 65)
        Decrypted_text += Decrypted_char
    
    elif (ord(char) >= 97 and ord (char) <= 122):
        Decrypted_char = chr((ord(char) - 97 - Shift)%26 + 97)
        Decrypted_text += Decrypted_char
    
    else:
        Decrypted_text += char

print ("Decrypted text is: " , Decrypted_text)


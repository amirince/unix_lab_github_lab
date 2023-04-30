import sys
message=sys.stdin # getting message from user
new_message="" # string variable to hold encrypted string

shft_amt = int(sys.argv[1]) # getting the shft_amt from cmd

for line in message: # iterating through each line in message
    line=line.upper() # converting current line to upper case

    for letter in line: # iterating through each letter in line
        if letter.isalpha(): # checking if letter is alphabet leter
            letter_ascii = ord(letter) # converting letter to ascii
            new_letter = (letter_ascii + shft_amt - 65) % 26 + 65 # getting ascii off new letter
            new_message += chr(new_letter) # adding ecrypted char to new_message

blocks = [new_message[i:i+5] for i in range(0, len(new_message), 5)] # splitting results in blocks of 5 char

for i in range(0, len(blocks), 10): # printing ten blocks per line
    print(' '.join(blocks[i:i+10]))


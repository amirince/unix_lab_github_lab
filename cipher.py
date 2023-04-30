import sys
message=sys.stdin # getting message from user
new_message="" # string variable to hold encrypted string

shft_amt = int(sys.argv[1]) # getting the shft_amt from cmd

for line in message: # iterating through each line in message
    line=line.upper() # converting current line to upper case

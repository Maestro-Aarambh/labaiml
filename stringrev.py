import sys

# Initialize an empty string to store the input
word = ""

# Loop to read each character until space is encountered
while True:
    # Read one character at a time
    char = sys.stdin.read(1)
    
    # Break the loop if the character is a space
    if char == " ":
        break
    
    # Append the character to the word
    word += char

print("You entered:", word)

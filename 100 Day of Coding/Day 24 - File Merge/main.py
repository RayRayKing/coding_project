#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Create a letter template
with open("Input/Letters/starting_letter.txt", mode="r") as file:
    letter_template = file.readlines()

# Get list of names
with open("Input/Names/invited_names.txt", mode="r") as f:
    names = f.readlines()

clean_names = []
for name in names:
    clean_names.append(name.strip("\n"))

for name in clean_names:
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as file:
        for line in letter_template:
            file.write(line.replace("[name]", name))


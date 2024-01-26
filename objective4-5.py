# Initialize an empty list called 'entries'
entries = []

# Open the file under path "grocery.txt" in write mode (specified by "w") and store the file handle in the variable called grocery_list
with open("grocery.txt", "w") as grocery_list:

    # Start a for loop that executes 5 times
    for i in range(0, 5):
        # We ask for the user input using the question in the input function and we store the user input in new_entry (the input is stripped, which means trailing and leading whitespaces are removed)
        new_entry = input("What would you like to add to your grocery list? ").strip()

        # We start an if statement which checks whether new_entry (user input) exists within the list we initialized (entries list).
        # If the statement evaluates to True, we continue (aka skip this iteration and go straight to asking for new user input)
        if new_entry in entries:
            continue

        # else, we add the (not yet existing) grocery item to our file, as well as to our list, which we use for checking for duplicates. 
        grocery_list.write(f"{new_entry}\n")
        entries.append(new_entry)
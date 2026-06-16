name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower()) #we use lower() to make all the the letters lower case because we would  not trust on the user to enter the name in the correct format. We can use lower() to make sure that all the letters are in lower case. We can also use upper() to make sure that all the letters are in upper case. We can use title() to make sure that the first letter of each word is capitalized.


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name) #we can use f-strings to format the string. We can use f-strings to insert variables into a string. We can also use f-strings to format the string in a specific way. In this case, we are using f-strings to insert the first name and last name into the full name variable. We are also using f-strings to format the full name variable in a specific way.
full_name = f"{first_name.title()} {last_name.title()}"
print(full_name)

# \t used for creating extra tab space:
print("Name:\tHasan Javed")
# \n used for creating extra line space:
print("Languages:\nPython\nC++\nJavaScript")




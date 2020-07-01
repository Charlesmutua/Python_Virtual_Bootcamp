"""
Write a program that takes your full name as input and displays the abbreviations 
of the first and middle names except the last name which is displayed as it is. 
For example, if your name is Robert Brett Roser, then the output should be R.B.Roser.
"""
full_name = input("Enter Your Full Name: ")

all_names = full_name.split()

f_name = all_names[0]
second_name = all_names[1]
last_name = all_names[2]


print(f"{f_name[0]}.{second_name[0]}.{last_name}")
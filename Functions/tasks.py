#Task 1

user_input = input("Enter Your String: ")

Yes = ["Yes", "yes", "YES"]
if user_input in Yes:
    print("Yes")
else:
    print("No")


#Task 2
"""
def largest(list):
    x= 3
    while x>0:


    largest = 0
    for var in list:
        if var>largest:
            largest = var
    return largest
    
myl = [12, 3,34]
print (largest(myl))

"""


#Task 3

def print_first_last(list):
    return (list[0], list[-1])

print (print_first_last([12,3,3,1]))

#task 4



#Task 5



#list = [12,3,5,7]
def half(list):
    x = len(list)//2
    return f"{list[0:x]} \n{list[x::]}"

list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(half(list))


    
    
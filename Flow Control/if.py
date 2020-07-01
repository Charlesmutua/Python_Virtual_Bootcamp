mystring = str(input("Enter String : "))
if len(mystring)>5:
    print("Satisfied")
else:
    print("Too Short")

score = int(input("Enter Score : "))
if score<0:
    print("Negative Score Not Allowed")
else:
    if score<60:
        print("Fail")
    else:
        print("Pass")

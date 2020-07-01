def calculate_score(list):
    bens=0
    abi=0
    for each in list:
        if each[0]==each[-1]:
            print("That's a Draw")
        elif each[0]== "R" and each[-1]=="P" or each[0]== "S" and each[-1]=="R" : 
            print("Ben Wins")
            bens+=1
        elif each[0]== "R" and each[-1]=="S"  or each[0]== "S" and each[-1]=="P":
            print("Abigail Wins")
            abi+=1
        elif each[0]== "R" and each[-1]=="P":
            print("Paper Wins")
    return abi, bens


List = [["R", "P"], ["R", "S"], ["S", "P"]]
print(calculate_score(List))


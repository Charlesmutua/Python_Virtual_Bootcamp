"""
Abigail vs Ben ====> R, P, S
[Abigail, Ben's]

[R, P] -----> Ben Wins
[P, S] -----> Ben
[R, S] -----> Abigail

Rock will crush Scissors
Scissors will cut a paper
Paper covers Rock


List = [["R", "P"], ["R", "S"], ["S", "P"]]

Ieterate through the list = >eg 1st itm = ["R", "P"]

abi = ["R", "S"] , ["S", "P"], ["P", "R"]



if each[0] and each[-1]



"""


def calculate_score(list):
    bens=0
    abi=0
    for each in list:
        if each[0]==each[-1]:
            print("That's a Draw")
        elif each[0]== "R" and each[-1]=="P" or each[0]== "P" and each[-1]=="S":
            print("Ben Wins")
            bens+=1
        elif each[0]== "R" and each[-1]=="S" or each[0]== "S" and each[-1]=="P":
            print("Abigail Wins")
            abi+=1
        elif each[0]== "S" and each[-1]=="P" or each[0]== "P" and each[-1]=="R":
            print("Abigail Wins")
            abi+=1
        elif each[0]== "S" and each[-1]=="R" or each[0]== "R" and each[-1]=="P":
            print("Ben Wins")
            abi+=1
    
        print("This a Draw")

    return abi, bens
        

        
    

List = [["R", "P"], ["R", "S"], ["S", "P"]]
list2 = [["S", "R"], ["R", "S"], ["R", "R"]]
print(calculate_score(list2))

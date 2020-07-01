"""
print("Hello World")


print(print.__doc__)
"""
from example import get_list
subjects = ["Math", "Eng"]
scores=[]

for subject in subjects:
    sc=int(input(f" Enter Score for {subject} : "))
    scores.append(sc)


mynum = get_list(scores)
print(mynum)

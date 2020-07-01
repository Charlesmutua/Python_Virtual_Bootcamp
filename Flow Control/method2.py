n= int(input("How Many Scores to Rank : "))
sc = input(f"Enter {n} scores :").split()
int_scores=[]
for x in sc:
    x=int(x)
    int_scores.append(x)


for y in int_scores:
    if y==y:
        int_scores.remove(y)

int_scores.sort(reverse =True)

print(int_scores)

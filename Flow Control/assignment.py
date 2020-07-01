"""
1.Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n  scores. Store them in a list and find the score of the runner-up.

The first line contains n . The second line contains an array A[]  of n integers each separated by a space.
5 
2 3 6 6 5

==> 5

"""
"""
n = int(input("Enter the number of scores ,n: "))
scores = map(int, input(f"Enter {n} scores seperated by a space: ").split()[:n])
print(scores)
scores = list(set(list(scores)))  #===> Covert the list into a Set; To remove duplicates, Then Back to List.


# set ==> 2,3,6,5

#scores = set(scores)
#scores = list(scores)
scores.sort(reverse = True) # ==> 6, 5 ,3,2

print(scores[1])


2.Given an integer n, perform the following conditional actions:

If n is odd, print Weird
If n  is even and in the inclusive range of 2 to 5 , print Not Weird
If n  is even and in the inclusive range of 6  to 20, print Weird
If n  is even and greater than 20, print Not Weird

"""
my_int = int(input("Enter an Integer, n :"))
if my_int < 0:
    print("Invalid Entry, Try Again")
    my_int = int(input("Enter an Integer, n"))
else:
    if my_int % 2 != 0:
        print("Weird")
    elif 2 < my_int <5:
        print("Not Weird")
    elif 6< my_int < 20:
        print("Weird")
    else:
        print("Not Weird")



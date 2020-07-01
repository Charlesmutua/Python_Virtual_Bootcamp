
#d
def get_first_value(list):
    return list[0]

ls1 = [1, 2, 3]
print(get_first_value([1, 2,3]))



#b)

def tri_area(x,y):
    area = 0.5*x*y
    return area

print(tri_area(4,6))


#c)

def next_edge(x, y):
    edge3 = x+y-1
    return edge3

print(next_edge(8,10))

#Max

def FindLargestNum(list):
    return(max(list))

print (FindLargestNum([4, 5, 1, 3]))




def hello_name(name):
    return f"Hello {name}"

name = "Charles"
print(hello_name(name))


#anumals
def animals(ch, co, p):
    return (ch*2 + co*4 + p*4)

print(animals(1,2,3))
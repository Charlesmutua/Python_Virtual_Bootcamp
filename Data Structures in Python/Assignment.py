taskList = [23, 'Jane', ['Lesson 23', 560, {'currency' : 'KES'}], 987, (76,'John')]

#Determing type of variable in taskList using an inbuilt function
print(type(taskList))
#Print KES
print(taskList[2][2]['currency'])
#Print 560
print(taskList[2][1])
#Use a function to determine the length of taksList
print(len(taskList))
#Change 987 to 789 without using an inbuilt -method (I.e Reverse)
taskList[3]= 789
print(taskList)
#Change the name “John” to “Jane” .
"""
'john' is in a tuple and a tupple is not mutable
"""

#ls1 = [123,34,54645,34,5] . Find the largest number in ls1 without using the max function.
ls1 = [123,34,54645,34,5]
ls1.sort()
print(ls1[-1])



#Given the dictionary below, find the total profit made
profit= {
            "cost_price": 32.67,
            "sell_price": 45.00,
            "inventory": 1200
                            }

total_cost = profit['cost_price']*profit['inventory']
total_sales = profit['sell_price']*profit['inventory']

total_profit = total_sales - total_cost

print(total_profit)
"""
6.Write a python program to find the index of the first occurrence of a substring 
in a string below -> plane

"The worlds fastest plane"

"""

sentence = "The worlds fastest plane"

words = sentence.split()

index_of_word = words.index('plane')

print(words)

print(index_of_word)
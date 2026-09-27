# list of fruits
fruits=['banana', 'orange', 'mango', 'lemon']
print(fruits)
#adding the item
fruits.append('apple') #adding to the last value in the List
print(fruits)  #printing the current list values
fruits.append('lemon') #adding to the last value in the List
print(fruits)
print(len(fruits)) #finding the length of the list(fruits)
print(fruits[len(fruits)-1])#print the last value
print(fruits[-1]) #print the last value
fruits.insert(2, 'xyz') #insert method used to insert particular place
print(fruits)
fruits.remove('xyz') #remove the item in the list
print(fruits) #it shows the list values
fruits.pop() # it remove the last item in the list
print(fruits)
fruits.pop(2) #pop pass the index place to remove
print(fruits)
del fruits[0]  #delete the particular index value
print(fruits)
fruitscopy=fruits.copy()
print(fruitscopy)
fruits.clear() # clearning the all the elements in the list
print(fruits)
del fruits  # delete the entire list
print(fruits)

#Lists in Python are noted with square brackets when used after an "=", with commas separating the individual elements in the list.
new_list= ['apple', 'orange', 12, ['peanut', 'butter', 'jelly', 'time']]

print(new_list)
print(len(new_list))
print(type(new_list[2]))
num = new_list[2]
obj = new_list[1]

print(f"I have {num} {obj}'s")

print("I have ", new_list[2], new_list[1])

#i like jelly on my toast
# newlist  has 4 elements
# element 3 of new list is a list

jell = new_list[3][2]
print(jell)
print(f"I like {jell} on my toast")

# Indexing & Slicing

# We can access indivdual elements of a list is the same as accessing them from a string, by using their index.
print(new_list[2])
print(new_list[-1])

#Slicing is available for lists. We use the same syntax of start:stop:step when slicing a list. We can build onto our understanding of slices by looping through just a slice of our list.
print(new_list[:3])

for item in new_list[:3]:
  print(item)

#The syntax for modifying elements to a list is similar to accessing elements in a list through indexing
new_list[0]= 'banana'
print(new_list)

# Adding Elements to a List

# There are several ways to add new elements to a list.

# The simplest way to add a new element to a list is to use the append() method. This method adds a new element to the end of a list.

# append() makes it easy to build lists dynamically, especially when appending in a for loop.
new_list.append(23)
print(new_list)

list1= []

for i in range(10):
  list1.append(i)

print(list1)

#You can also add a new element at any position in a list by using the insert() method.

# We can do this by specifying the index of the new element and its value. The insert() method shifts all previous values one position to the right.
new_list.insert(0, 'grape')

print(new_list)

# Removing Elements from a List

# We can remove a(n) element(s) from a list either by either the position or the value.


# If we know the position of the element we want to remove from a list we can use the del statement. One key thing to note, the value is no longer able to be accessed using this statement.
del new_list[2]
del new_list[-1]
print(new_list)

# If we want to use the value of the item after it has been removed from the list, we can use the pop() method. This method removes the last item in the list by default. Optionally, we can pass the index that we want to pop as an argument to the method to return its value.
food= ['burger', 'fries', 'pizza', 'hotdog']
food_item= food.pop()
food_item2= food.pop(1)

print(food_item)
print(food_item2)

#We can also remove an item from a list by value using the remove() method.
transportation= ['planes', 'trains', 'automobiles', 'boats']

transportation.remove('automobiles')
item_remove= 'trains'
transportation.remove(item_remove)

print(transportation)
print(item_remove)

# Organizing Lists

# There are many times that we do not have control the order in which the elements of a list are created, but we want the list to be ordered in a particular way. There are methods in the List Class that can help us with this.

# The sort() method changes the order of a list permenately in alphabetical order. There is not an "undo" method to get our list back in its original state.
instruments= ['piano', 'flute', 'guitar', 'trumpet']

instruments.sort()

print(instruments)

# We can also use the sort() method to have our list in reverse alphabetical order by passing the arguement reverse=true
instruments.sort(reverse=True)

print(instruments)

# How does this change if all of our values are not strings or not all in the same case?
instruments= ["Piano", 'flute', 'guitar', 'Guitar', 'trumpet']
mixed_list= ['piano', '1', 'trumpet', '5']

example_sorted_function = sorted(instruments)
print(example_sorted_function)
print(instruments)
example_sort_method = instruments.sort()
print(example_sort_method)
print(instruments)

# If we only want to sort a list temporarily we can use the sorted function. The sorted function allows us to display the list in alphabetical order, but the original list is unchanged. This function also accepts the reverse=True arguement.
instruments= ['piano', 'flute', 'guitar', 'trumpet']

print(sorted(instruments))

# If we want an easy way to reverse the order of the original list we can use the reverse() method. You cannot undo this change, but you can just REVERSE! REVERSE! aka call the reverse method again to change it back the original order.
furniture= ['couch', 'chair', 'bed', 'table']

furniture.reverse()

print(furniture)

# # This does NOT copy a list:
# # furniture2= furniture
# # print(furniture2)

# # Valerie's Example
# original_list = [1, 2, 3]
# new_reference = original_list  # new_reference is now another name for the same list object

# new_reference.append(4)  # Modifying the list via new_reference

# print("Original List:", original_list)  # Output: Original List: [1, 2, 3, 4]
# print("New Reference:", new_reference)  # Output: New Reference: [1, 2, 3, 4]
# print(original_list == new_reference)

# # # What does this show.....
# # # It shows that line 7 is NOT how we copy an obhect.
# # # line 7 only adds a new reference to the existing object.

# # # how DO we copy a list??


# Valerie's REAL Copy options:
original_list = ["A", "B", "C"]
copied_list = original_list.copy()  # copied_list is now a separate object with the same contents

copied_list.append(4)  # Modifying the copied list does not affect the original list

print("Original List:", original_list)  # Output: Original List: [A, B, C]
print("Copied List:", copied_list)  # Output: Copied List: [A, B, C, 4]
print(original_list == copied_list)
# In this example, original_list remains unchanged even though copied_list
#  is modified. This shows that copied_list is indeed a separate list.

# However if we start to manipulate these two variables we will see that is not the case.
furniture.append("armoire")

print(furniture)
print(furniture)

# Armoire got added to both variables? Not quite. By setting furniture2 = furniture we actually created another pointer to the same place in memory. What we do under one variable name impacts the other.

# Instead, we can create a slice of the full list and assign that to a new variable.
transportation= ['planes', 'trains', 'automobiles', 'boats']

# Option#2  creating a list of the object (its a slice from beginning to end, so it will be identical)
new_transportation= transportation[:]
new_transportation.append('bicycle')

print(new_transportation)
print(transportation)
print(transportation == new_transportation)
# Create a list, dictionary, and set
my_list = [1, 2, 3]
my_dict = {"name": "Sakshi", "age": 21}
my_set = {10, 20, 30}

# Operations on List
print("Original List:", my_list)
my_list.append(4)  # Add an element
print("After Append:", my_list)
my_list.remove(3)  # Remove an element
print("After Remove:", my_list)
my_list[1] = 5  # Modify an element
print("After Modification:", my_list)

# Operations on Dictionary
print("\nOriginal Dictionary:", my_dict)
my_dict["city"] = "Mumbai"  # Add a key-value pair
print("After Adding a Key-Value Pair:", my_dict)
del my_dict["age"]  # Remove a key-value pair
print("After Deleting a Key-Value Pair:", my_dict)
my_dict["name"] = "Nidhi"  # Modify a value
print("After Modifying a Value:", my_dict)

# Operations on Set
print("\nOriginal Set:", my_set)
my_set.add(40)  # Add an element
print("After Adding an Element:", my_set)
my_set.remove(20)  # Remove an element
print("After Removing an Element:", my_set)
my_set.update([50, 60])  # Add multiple elements
print("After Adding Multiple Elements:", my_set)

# Final Output
print("\nFinal List:", my_list)
print("Final Dictionary:", my_dict)
print("Final Set:", my_set)
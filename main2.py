my_set = {1,2,3,4,4,4}
print("Set :", my_set)

my_set.add(5)
print("Updated Set :", my_set)

Set1 = my_set
Set2 = {2,4,4,6}

print("\nSet 1", Set1)
print("Set 2", Set2)
print("Difference")
print(Set1.difference(Set2))
print("Symmeteric Difference")
print(Set1.symmetric_difference(Set2))
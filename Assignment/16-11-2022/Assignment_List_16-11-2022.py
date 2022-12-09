
l = input("Enter name, age, salary respectively ").split(' ')

print(l)

l[1], l[2] = int(l[1]), int(l[2])

print(l)

designation = input("\nEnter your profession: ")

l.append(designation)

print(l)

print(f"\nCount of name: Amit in the list: {l.count('Amit')}")

print(f"\nIndex of age: {l.index(23)}")

print(f"\nPop the last element: {l.pop()}")

print(f"\nUpdated List: {l}")

designation = input("\nEnter your profession: ")
l.insert(2,designation)
print(f"\nInserted the element at index 2: {l}")

print("\nRemove the salary from the list")
l.remove(100000)
print(f"\nUpdated List: {l}")

sL = [2,35,6,677,86,453,7452,54]
print(f"\nnew list: {sL}")
sL.sort()
print(f"\nsorted list: {sL}")


l1 = [1,2,4,5,6]
l2 = [45,566,23]

print(f"\nFirst List: {l1}\nSecond List{l2}")
l1.extend(l2)

print(f"\nExtended List: {l1}")

l2.clear()
print(f"\nEmptied the second list: {l2}")

l_copy = l.copy()

print(f"\nCopy of list: {l_copy}")





Emp={'Anuj',101,'Thane',45000,1,30.5}

print(f"Given set is {Emp}")


n = input("\nEnter your designation: ")
Emp.add(n)
print(f"\nUpdated set after add designation: {Emp}")


Emp1 = {'Amit', 102, 'Mumbai', 45000, 1, 30.5}

print(f"\nFirst set is {Emp}")
print(f"Second set is {Emp1}")
print(f"Difference between both set is {Emp.difference(Emp1)}")

name_loc = {'Anuj', 'Thane'}

print(f"\nFirst set is {Emp}")
print(f"Second set is {Emp1}")
print(f'Name and location set is {name_loc}')

print(f"\nIs Name and location set is subset of first set? {name_loc.issubset(Emp)}")
print(f"Is First set is superset of name and location? {Emp.issuperset(name_loc)}")
print(f"Is Name and location set disjoint of second set? {name_loc.isdisjoint(Emp1)}")

print("\nRemove the Developer from first Set")
Emp.discard('Developer')
print(f"\nUpdated first set is {Emp}")

print(f"\nFirst set is {Emp}")
print(f"Second set is {Emp1}")

print(f"Common or intersection between first and second set is {Emp.intersection(Emp1)}")

print(f"\nPop an element from first set: {Emp.pop()}")
Emp1.remove(1)
print(f"\nSecond set after removing an element: {Emp1}")

print(f"\nUnion of first and second set is {Emp.union(Emp1)}")

copied_Emp = Emp.copy()

print(f"\nCopy of first set is {copied_Emp}")

copied_Emp.clear()

print(f"\nCopy of first set after clearing the element: {copied_Emp}")

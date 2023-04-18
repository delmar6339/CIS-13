def dl1(mylist):
    n = int(input("Number of items for your list:"))
    for _ in range(n):
        s = int(input("Enter an integer:"))
        mylist.append(s)
    return mylist

def displaylist(mylist):
    for item in mylist:
        print(item)

# 1.
mylist = []
mylist = dl1(mylist)
displaylist(mylist)
print(mylist)

# 2.
mylist.insert(1, 99)
print(mylist)

# 3.
mylist[1] = 100
print(mylist)

# 4.
second_list = [500, 600, 700, 800, 900]
print("Second list:", second_list)

mylist.extend(second_list)
print("First list after extending with the second list:", mylist)

# 5.
mylist.remove(800)
print("First list after removing 800:", mylist)

# 6.
mylist.pop(2)
print("First list after removing third item:", mylist)

# 7.
grades = ["A", "B", "C", "A", "A", "C"]

# 8.
print("Number of A grades:", grades.count("A"))

# 9.
print("Index of the first B grade:", grades.index("B"))

# 10.
if "F" not in grades:
    print("F is not in the list.")

# 11.
second_list.clear()
print("Cleared second list:", second_list)

# 12.
del second_list

# 13.
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

# 14.
players.sort()
print("Sorted list of players:", players)

# 15.
players2 = players.copy()
print("Players2:", players2)

# 16.
players2.reverse()
print("Players:", players)
print("Players2:", players2)
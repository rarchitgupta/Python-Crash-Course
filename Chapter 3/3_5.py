guestList = ["John Mayer", "Joel Zimmerman", "Hans Zimmer", "Chris Martin"]

print("Original Guest List: ")
print(guestList)
print(guestList[3] + " cannot make it")
guestList.remove(guestList[3])
print("Guest List after removal: ")
print(guestList)
guestList.insert(3, "Charlie Puth")
print("New invite to: " + guestList[3])
print(guestList)
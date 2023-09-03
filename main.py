myList = [15,8,9, 1]
print(myList)
myList[2] = 11
print(myList)
print(myList[0])
myList.append(4)
print(myList)
myList.remove(myList[3])
print(myList)
myList[1] = "Software 1 List"
print(myList)
print(len(myList [1]))
print(myList)
print(len(myList))
myList[1] = 15
print(myList)

index = 0
while index < len(myList):
    if myList[index] > 5:
        print(f"{myList[index]} is greate than 5")
    else:
        print(f"{myList[index]} is not greater than 5")
    # move to the next index
    index += 1





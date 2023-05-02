nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]


def insertionSort(anArray):
    for i in range(1, len(anArray)):
        # Save the insert value
        insertVal = anArray[i]
        # Save the insert position
        insertPos = i
        
        # Modify the insert position and overwrite it if it does not belong
        while insertPos > 0 and insertVal < anArray[insertPos - 1]:
            anArray[insertPos] = anArray[insertPos - 1]
            insertPos -= 1
        # Insert the value in its proper position and overwrite the duplicate if there was any change in the positions
        anArray[insertPos] = insertVal
        

print(insertionSort(nums))
print(insertionSort(words))


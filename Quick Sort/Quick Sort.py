# Mark john M. Raymundo CoE 2-2 Data Structure and Algorithms
#Sorting: Quick Sort
#Given Array Values: 67, 77, 47, 15, 1, 25, 59, 46, 8, 87
#Source: https://www.youtube.com/watch?v=9KBwdDEwal8&list=PLliXbzY3XhUSJy3izXH-0ojiT3Uup8xbu&index=4

def QuickSort(ArrayValue, Left, Right):
    if Left < Right:
        PartitionPosition = Partition(ArrayValue, Left, Right)
        QuickSort(ArrayValue, Left, PartitionPosition - 1)
        QuickSort(ArrayValue, PartitionPosition + 1, Right)

def Partition(ArrayValue, Left, Right):
    i = Left
    j = Right - 1
    Pivot = ArrayValue[Right]

    while i < j:
        while i < Right and ArrayValue[i] < Pivot:
            i += 1
        while j > Left and ArrayValue[j] >= Pivot:
            j -= 1
        #Swapping j and i element if they didn't cross
        if i < j:
            ArrayValue[i], ArrayValue[j] = ArrayValue[j], ArrayValue[i]
        print("Pivot: ", Pivot)
        print("i element: ", ArrayValue[i])
        print("j element: ", ArrayValue[j])
        print("Current Array Value: ", ArrayValue)
    #Swapping i and pivot if j and i crossed
    if ArrayValue[i] > Pivot:
        ArrayValue[i], ArrayValue[Right] = ArrayValue[Right], ArrayValue[i]
    print("Pivot: ", Pivot)
    print("New Pivot Value: ", ArrayValue[Right])
    print("Current Array Value: ", ArrayValue)
    return i


ArrayValue = [67, 77, 47, 15, 1, 25, 59, 46, 8, 87]
QuickSort(ArrayValue, 0, len(ArrayValue) - 1)

print("Final Array Value",ArrayValue)
# Mark john M. Raymundo CoE 2-2 Data Structure and Algorithms
#Sorting: Quick Sort
#Given Array Values: 67, 77, 47, 15, 1, 25, 59, 46, 8, 87
#Source: https://www.youtube.com/watch?v=9KBwdDEwal8&list=PLliXbzY3XhUSJy3izXH-0ojiT3Uup8xbu&index=4

def QuickSort(ArrayValue, Left, Right):
    if Left < Right:
        PartitionPosition = Partition(ArrayValue, Left, Right)
        QuickSort(ArrayValue, Left, PartitionPosition - 1)
        QuickSort(ArrayValue, Left, PartitionPosition + 1)
        
def Partition(ArrayValue, Left, Right):


ArrayValue = [67, 77, 47, 15, 1, 25, 59, 46, 8, 87]
QuickSort(ArrayValue)

print("Final Array Value",ArrayValue)
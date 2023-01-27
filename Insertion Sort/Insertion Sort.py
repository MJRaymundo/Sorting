# Mark john M. Raymundo CoE 2-2 Data Structure and Algorithms
#Sorting: insertion Sort
#Given Array Values: 67, 77, 47, 15, 1, 25, 59, 46, 8, 87
#Source: https://www.youtube.com/watch?v=R_wDA-PmGE4&list=PLliXbzY3XhUSJy3izXH-0ojiT3Uup8xbu&index=1

def InsertionSort(ArrayValue):
    for i in range(1, len(ArrayValue)):
        j = i
        while ArrayValue[j-1] > ArrayValue[j] and j > 0:
            #Swapping Values
            ArrayValue[j-1], ArrayValue[j] = ArrayValue[j], ArrayValue[j-1]
            j -= 1
            

ArrayValue = [67, 77, 47, 15, 1, 25, 59, 46, 8, 87]
InsertionSort(ArrayValue)

print("Final Array Value",ArrayValue)
# Mark john M. Raymundo CoE 2-2 Data Structure and Algorithms
#Sorting: Selection Sort
#Given Array Values: 67, 77, 47, 15, 1, 25, 59, 46, 8, 87
#Source: https://www.youtube.com/watch?v=ee80YmiaSVQ&list=PLliXbzY3XhUSJy3izXH-0ojiT3Uup8xbu&index=2

def selection_sort(ArrayValue):
    for i in range(0, len(ArrayValue) - 1):
        cur_min_idx = i
        for j in range (i + 1, len(ArrayValue)):
            if ArrayValue[j] < ArrayValue[cur_min_idx]:
                cur_min_idx = j

        #Swapping Lowest Value to Current Position
        ArrayValue[i], ArrayValue[cur_min_idx] = ArrayValue[cur_min_idx], ArrayValue[i]
        print("Current Position: ", i)
        print("Array Value", ArrayValue)

ArrayValue = [67, 77, 47, 15, 1, 25, 59, 46, 8, 87]
selection_sort(ArrayValue)
print(ArrayValue)
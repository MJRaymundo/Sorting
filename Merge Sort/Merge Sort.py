# Mark john M. Raymundo CoE 2-2 Data Structure and Algorithms
#Sorting: Merge Sort
#Given Array Values: 67, 77, 47, 15, 1, 25, 59, 46, 8, 87
#Source: https://www.youtube.com/watch?v=cVZMah9kEjI&list=PLliXbzY3XhUSJy3izXH-0ojiT3Uup8xbu&index=3

def MergeSort(ArrayValue):
    if len(ArrayValue) > 1:
        LeftArrayValue = ArrayValue[:len(ArrayValue)//2]
        RightArrayValue = ArrayValue[len(ArrayValue)//2:]
        print("Left: ", ArrayValue)
        print("Right: ", RightArrayValue)
        
        #Recursion
        MergeSort(LeftArrayValue)
        MergeSort(RightArrayValue)


        #Merge
        i = 0 #LeftArrayValue idx
        j = 0 #RightArrayValue idx
        k = 0 #Merged ArrayValue idx
        while i < len(LeftArrayValue) and j < len(RightArrayValue):
            if LeftArrayValue[i] < RightArrayValue[j]:
                ArrayValue[k] = LeftArrayValue[i]
                i+=1
            else:
                ArrayValue[k] = RightArrayValue[j]
                j +=1
            k +=1
        while i < len(LeftArrayValue):
            ArrayValue[k] = LeftArrayValue[i]
            i += 1
            k += 1

        while j < len(RightArrayValue):
            ArrayValue[k] = RightArrayValue[j]
            j+=1
            k+=1
        print("Left Array Value/s: ", LeftArrayValue,"Right Array Value/s: ", RightArrayValue,"Current Array Value/s: ", ArrayValue)

ArrayValue = [67, 77, 47, 15, 1, 25, 59, 46, 8, 87]
MergeSort(ArrayValue)

print("Final Array Value",ArrayValue)
# Mark john M. Raymundo CoE 2-2 Data Structure and Algorithms
#Sorting: Bubble Sort
#Given Array Values: 67, 77, 47, 15, 1, 25, 59, 46, 8, 87
#Source: https://www.youtube.com/watch?v=Vca808JTbI8

def BubbleSort(ArrayValue):
    for i in range (len(ArrayValue)-1, 0, -1):
        for j in range (i):
            if ArrayValue[j]>ArrayValue[j+1]:

                #Swapping Values
                Temp = ArrayValue[j]
                ArrayValue[j] = ArrayValue[j+1]
                ArrayValue[j+1] = Temp
            print("Step:", j + 1, " Array Value", ArrayValue)
        print("Iteration: ", 10 - i)
        print("Array Value", ArrayValue)

ArrayValue = [67, 77, 47, 15, 1, 25, 59, 46, 8, 87]
BubbleSort(ArrayValue)

print("Final Array Value",ArrayValue)
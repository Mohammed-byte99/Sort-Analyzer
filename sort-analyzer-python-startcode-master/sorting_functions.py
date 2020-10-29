def bubbleSort(anArray):
    for numCompare in range(len(anArray) - 1, 0, -1):
        for i in range (numCompare):
            if anArray[i] > anArray[i+1]:
                anArray[i], anArray[i+1]  = anArray[i+1],anArray[i]
    
def selectionSort(anArray):
    for fillSlot in range(len(anArray) - 1):
        minpos = fillSlot
        for j in range(fillSlot+1, len(anArray)):
            if anArray[j] < anArray[minpos]:
                minpos = j
        anArray[fillSlot], anArray[minpos] = anArray[minpos], anArray[fillSlot]
    
def insertionSort(anArray):
      
    for i in range(1, len(anArray)):
        value = anArray[i]
        position = i
 
        while position > 0 and anArray[position - 1] > value:
            anArray[position] = anArray[position - 1]
            position -= 1
 
        anArray[position] = value


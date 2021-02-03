#
# Zarifa Ishankhodjaeva 
#
# FDAC

# Function to do insertion sort 
def insertionSort(arr):  
    for i in range(1, len(arr)): 
        key = arr[i]  
        j = i-1
        while j >=0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key 
        print ("Sorting :" ,arr)


arr=[23,6,7,1,2]
arr2= [2,6,8,3,5,1]

insertionSort(arr)


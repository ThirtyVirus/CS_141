"""
Selection Sort - Brandon Calabrese

QUESTIONS
1- Insertsort performs better than selectionsort when the numbers are more 'sorted'
to start with.

2- Time complexity of selection sort is always n(n - 1)/2, whereas insertionsort
is at the worst n(n-1)/2 efficiency but sometimes faster.
"""

def getListFromFile(path):
    """
    Collects list of integers from file into list,
    assumes one value of line
    """
    lst = []
    myStr = open(path)
    for line in myStr:
        lst.append(int(line))
    return lst

def displayList(lst):
    """
    Displays list of values on the same line,
    seperated by spaces
    """
    for l in lst:
        print(l,end = " ")
    print("")

def swap(lst,index1,index2):
    """
    Swaps 2 values in a list
    """
    temp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = temp
    return lst
    
def findMin(lst,mark):
    """
    Returns the index of the smallest integer in a list
    """
    minNum = lst[mark]
    index = mark
    counter = mark
    
    while counter < len(lst):
        if lst[counter] < minNum:
            minNum = lst[counter]
            index = counter
        counter += 1
    return index 

def sortList(lst):
    """
    Sorts a list of integers from smallest to largest
    Uses selection sort algorithm
    """
    counter = 0
    while counter < len(lst):
        pos2 = findMin(lst, counter)      
        lst = swap(lst,counter,pos2)
        counter += 1
        
    return lst
    
def main():
    """
    Gets user input and calls the rest of the program
    """
    lst = getListFromFile(input("Input File Name: "))
    
    print("Before: ",end = "")
    displayList(lst) #before
    lst = sortList(lst) #sorting lst
    print("After: ",end = "")
    displayList(lst) #after
main()

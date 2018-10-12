##-------------------------------------------------------------------
## Sorting Prices
## Dallas Spendelow
## October 12, 2018
## This program uses a merge sort to sort prices. 
##-------------------------------------------------------------------

def mergeSort(alist):
    ## print("Splitting ",alist)      ## Debugging
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    ##print("Merging ",alist)     ## Debugging
    
## This function takes user input. It allows the user to specify the number of
## elements, as well as what they are. It rounds to two decimal places because
## this program deals with prices. 
def inputList():
    list = []
    numberElements = int(input("How many prices are in your list? "))
    for i in range(numberElements):
        element = round(float(input("Enter a price: ")),2)
        list.append(element)
    return list

## The user can take further action by leaving as is, adding, changing, or deleting.
## After any changes, the list will be resorted. 
def furtherAction(userList):
    choice = input("You may either 'add', 'delete', or 'change' any items. "
                   "You may also 'leave' the list as is. It's your choice. ")
    if choice == "leave":
        print("That is fine. Your list remains the same.")
    elif choice == "add":
        addedItem = float(input("Add an item. "))
        userList.append(addedItem)
        print("Added",addedItem,"to your list and resorted.")
    elif choice == "delete":
        userList = deleteItem(userList)
    elif choice == "change":
        userList = changeItem(userList)
    else:
        print("Make sure you answer in the format.")
        furtherAction(userList)
    
    return userList

## Deletes an item
def deleteItem(userList):
    deletedItem = float(input("Which item would you like to delete? "))
    if deletedItem not in userList:
        print("That item is not in your list.")
        deleteItem(userList)
    else:
        userList.remove(deletedItem)
        print("Deleted",deletedItem,"from your list and resorted.")
    return userList

## Replaces an item with another item.
def changeItem(userList):
    changedItem = float(input("Which item would you like to change? "))
    if changedItem not in userList:
        print("That item is not in your list.")
        changeItem(userList)
    else:
        replacementItem = float(input("What are you replacing the item with? "))
        userList[userList.index(changedItem)] = replacementItem
        print("Replaced",changedItem,"with",replacementItem,".")
    return userList       
    
    
## Main code. Take input, sort, print, then allow the user to change or leave as is.
userList = inputList()
##print(userList)    ## debugging
mergeSort(userList)
print("Your sorted list is",userList)

userList = furtherAction(userList)
##print(userList)    ## Debugging
mergeSort(userList)
print("Your sorted list is",userList)
def has_negatives(a):

    items = dict() # create dictionary
    result = list() # create list

    # i need to read the list 
    for item in a:
        # if there is an item in a 
        if items.get(abs(item)):
            # if negative plus positive is 0 then
            if (items.get(abs(item)) + item) == 0:
                result.append(abs(item)) # push thatvalue into my list
        else:
           # i need to create a key value pair in case there is not no value
            items[abs(item)] = item 

    # i want to return the populated list
    return result



if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))

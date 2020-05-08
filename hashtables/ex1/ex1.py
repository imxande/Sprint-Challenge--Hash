def get_indices_of_item_weights(weights, length, limit):

    # create a dictionary
    items = dict()

    # read the weight list, I need to loop
    for i in range(length):
        # diff place holder for the item I am looking for
        diff = items.get(limit - weights[i])
        
        # if I need to find the sum then i can check if diff already exist
        if diff != None:
            # if so then return the (zero, one) form tuple
            return (i, diff)
        else:
            # if diff does not exist then create key value pair relationship
            items[weights[i]] = i

    print(items)

    # our function return none if there is not pair
    return None

    

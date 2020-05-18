#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    routes = dict() # create routes dictionary 
    ls = list() # place holder list

 
    # i need to read the items in tickets
    for item in tickets:
        # i need key value pair rrelationship between source and destination respectively
        routes[item.source] = item.destination

    # set an index to loop over the list
    i = 0
    # set the current destination to initialize the list
    curr = "NONE"

    # i need to read untill there is no more tickets in the list
    while i < length:
        # set the current destination to be the new source 
        curr = routes.get(curr)
        # append on each iteration the routes
        ls.append(curr)
        # increase count
        i += 1

    # return the ordered flight routes at the end
    return ls 
   

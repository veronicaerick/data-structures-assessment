#Sorting

def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    # go through as many time as the length of the list
    for i in range(len(lst)):
        #  set swapped to false, will switch to true when something has been swapped
        swapped = False
        # move through list up until the last item
        for x in range(len(lst) - 1):
            #  if item x is higher than the next in the list item, swap them and set swapped to true
            if lst[x] > lst[x + 1]:
                lst[x], lst[x + 1] = lst[x + 1], lst[x]
                swapped = True
        #  if list is already ordered at this point, break out of the loop
        if not swapped:
            break

    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    result = []
    # while length of either list isnt empty
    while len(list1) > 0 or len(list2) > 0:
        # if list 1 is empty, append the first item of list 2 to my result list
        if list1 == []:
            result.append(list2.pop(0))
        # same as above, vice versa
        elif list2 == []:
            result.append(list1.pop(0))
        # if item 1 in list 1 is less than item 1 in list 2, grab item 1 from list 1 and append it to results
        elif list1[0]<list2[0]:
            result.append(list1.pop(0))
        # same as above, vice versa
        else: 
            result.append(list2.pop(0))

    return result


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    # turn everything in the list to a list of one. if the length of my list is 1, return it
    if len(lst) < 2:  
        return lst

    # index at the middle of the list
    half_way = int(len(lst) / 2)  

    # divide list into two at the halfway point 
    list1 = merge_sort(lst[:half_way])  
    list2 = merge_sort(lst[half_way:])  


    results = []
    # check to see if there is anything in either list
    while len(lst1) > 0 or len(lst2) > 0:
        # if items left in both lists
        # if list 1 is empty, grab the first item in list 2
        if lst1 == []:
            results.append(lst2.pop(0))
        # if list 2 is empty, grab the first item in list 1 and add it to results list
        elif lst2 == []:
            results.append(lst1.pop(0))
        # if item 1 in list one is less than item 1 in list 2, append item 1 in list 1 to results
        elif lst1[0] < lst2[0]:
            results.append(lst1.pop(0))
        # vice versa
        else:
            results.append(lst2.pop(0))

    return results



#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
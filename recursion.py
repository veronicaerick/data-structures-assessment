# --------- #
# Recursion #
# --------- #

# 1. Write a function that uses recursion to print each item in a list.
def print_item(my_list, i=0):
    """Prints each item in a list recursively.

        >>> print_item([1, 2, 3])
        1
        2
        3 

    """
    # base case
    if i == len(my_list):
        return
    
    # print whats at index i
    print my_list[i]
    # recall the function, but add one to index i each time
    print_item(my_list, i+1)


# 2. Write a function that uses recursion to print each node in a tree.

def print_all_tree_data(tree):
    """Prints all of the nodes in a tree.


        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> print_all_tree_data(one)
        1
        2
        3

    """
    
    # for every child in the tree, recall function to print everything
    for child in tree.children:
        print_all_tree_data(child)

    print tree.data

# 3. Write a function that uses recursion to find the length of a list.


def list_length(my_list):
    """Returns the length of list recursively.
        >>> list_length([1, 2, 3, 4])
        4

    """
    # check to see if my list is empty
    if not my_list:
        return

    #  call list length function, slice at index 1, adding one
    return list_length(my_list[1:]) + 1

    


# 4. Write a function that uses recursion to count how many nodes are in a tree.

def num_nodes(tree):
    """Counts the number of nodes.

        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
    """
    #  set count to none
    count = 0

    # for every child in the tree, add it to the count by calling the funciton for each child
    for child in tree.children:
        count += num_nodes(child)

    return count

#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

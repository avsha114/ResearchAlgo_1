def recursive_sort(x):
        # If the item is a collection of one of these types,
        # we should sort it and then sort its elements as well with recursion
        if isinstance(x, list) or isinstance(x, tuple) or isinstance(x, set):
            sorted_x = sorted(x)
            for index,val in enumerate(sorted_x):
                sorted_x[index] = recursive_sort(val)
            
            return sorted_x
        # for dictionaries we need to sort by keys and the sort the values themselves
        elif isinstance(x, dict):
            sorted_x_list = sorted(x.items())
            sorted_x = {}
            # after we sorted the keys, we sort the values and add them again
            for key,val in sorted_x_list:
                sorted_x[key] = recursive_sort(val)
            
            return sorted_x
        
        else:
            return x

def print_sorted(x):
    print (recursive_sort(x))
    
if __name__ == '__main__':
    # Test1:
    t1 = {"a":5,
        "z":6,
        "d":[1,3,4,2]}
    print_sorted(t1)

    # Test2:
    t2 = {1: 1,
            10: {6: 2, 1: [4, -1, -2]},
            7: (1, 3, 2, 4),
            8: {"B": "world", "A": "hello"}}
    print_sorted(t2)
    
    # Test3:
    t3 = {"C": [5, -2, 7, 1],
            "F": "Nice",
            "A": [3, 2]}
    print_sorted(t3)


            
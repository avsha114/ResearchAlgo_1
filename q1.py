def safe_call(f, **kwargs):
    # We go through the input argumnets by names:
    for key,value in kwargs.items():
        # if argument's name is not in the function or from a wrong type:
        if key in f.__annotations__ and \
            not isinstance(value, f.__annotations__[key]):
            raise TypeError('ERROR: Wrong argument types')

    return f(**kwargs)
   
# a simple test function:   
def test_f(x: float, y: int, z: float):
    return x + y + z

if __name__ == '__main__':
    # Test1
    # Output: 10.0
    try:
        print(safe_call(test_f, x=1.2, y=6, z=2.8))
    except BaseException as err:
        print(err)
        
    # Test2
    # Output: 10.0
    try:
        print(safe_call(test_f, y=6, x=1.2, z=2.8))
    except BaseException as err:
        print(err)
        
    # Test3
    # Output: Success
    try:
        print(safe_call(test_f, a=1.2, y=2.8, z=6))
    except BaseException as err:
        print("Success")
        
    # Test4
    # Output: Success
    try:
        print(safe_call(test_f, x="a", y=2.8, z=6))
    except BaseException as err:
        print("Success")
        
    # Test5
    # Output: Success
    try:
        print(safe_call(test_f, x=1.2, y=2.8))
    except BaseException as err:
        print("Success")
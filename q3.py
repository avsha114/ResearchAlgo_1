EPS = 0.000001

# df gets a functions and return its derivative
def df(f, x):
    return (f(x + EPS) - f(x)) / EPS

def find_root(f, a, b):
    # Choose x that is close to the root and choose a big enough number of iterations:
    x = (a+b) / 2
    iterations = 100
    
    for n in range(0, iterations):
        fx = f(x)
        
        # the root will make abs(fx) close to 0
        if abs(fx) < EPS:
            return x
        
        deriv = df(f, x)
        
        if deriv <= 0:
            raise Exception('ERROR: No root found')
        
        # Continue to another iterations for accuracy
        x = x - fx / deriv

    return x

if __name__ == '__main__':
    # Test1:
    f1 = lambda x: x**2 - 4
    try:
        print(find_root(f1, 1, 3))
    except Exception as e:
        print(e)

    # Test2:
    f2 = lambda x: x**2 - 100
    try:
        print(find_root(f2, 1, 4))
    except Exception as e:
        print(e)
        
    # Test3:        
    f3 = lambda x: x**2 + 9
    try:
        print(find_root(f3, 1, 10))
    except Exception as e:
        print("Sucess")

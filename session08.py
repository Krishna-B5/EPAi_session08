def outer():
    n = 50
    def inner():
        """ 
        closure is equal to inner function plus extended scope/free variable
        """
        result = inner.__doc__
        if len(result) > n:
            return True
        else:
            return False
    return inner()


def fibonacci(e):
    n1 = 0
    n2 = 1
    count = 0
    end = e
    a = [0, 1]
    def fib():
        nonlocal n1, n2, count
        while count < end:
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            a.append(n3)
            count += 1
    fib()
    return a



# bopace 23 Oct 2016

edge1 = 0
edge2 = 1
a = 10
b = 100
c = 3

a2 = 10
b2 = 20
c2 = 3

a3 = 200
b3 = 50
c3 = 9

def fibonacci_iterative(n):
    if n < 2:
        return n
    a = 0
    b = 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_dynamic(n):
    terms = [0,1]
    if n < 2:
        return n
    for i in range(2, n+1):
        terms.append(terms[i-1]+terms[i-2])
    return terms[n]

if __name__ == "__main__":
    print "ITERATIVE:"
    print str(edge1) + "-th term in fib sequence: " + str(fibonacci_iterative(edge1))
    print str(edge2) + "-th term in fib sequence: " + str(fibonacci_iterative(edge2))
    print str(a) + "-th term in fib sequence: " + str(fibonacci_iterative(a))
    print str(b) + "-th term in fib sequence: " + str(fibonacci_iterative(b))
    print str(c) + "-th term in fib sequence: " + str(fibonacci_iterative(c))

    print "RECURSIVE:"
    print str(edge1) + "-th term in fib sequence: " + str(fibonacci_recursive(edge1))
    print str(edge2) + "-th term in fib sequence: " + str(fibonacci_recursive(edge2))
    print str(a2) + "-th term in fib sequence: " + str(fibonacci_recursive(a2))
    print str(b2) + "-th term in fib sequence: " + str(fibonacci_recursive(b2))
    print str(c2) + "-th term in fib sequence: " + str(fibonacci_recursive(c2))

    print "DYNAMIC PROGRAMMING:"
    print str(edge1) + "-th term in fib sequence: " + str(fibonacci_dynamic(edge1))
    print str(edge2) + "-th term in fib sequence: " + str(fibonacci_dynamic(edge2))
    print str(a3) + "-th term in fib sequence: " + str(fibonacci_dynamic(a3))
    print str(b3) + "-th term in fib sequence: " + str(fibonacci_dynamic(b3))
    print str(c3) + "-th term in fib sequence: " + str(fibonacci_dynamic(c3))
    

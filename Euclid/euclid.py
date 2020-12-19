import sys

"""
In mathematics, the Euclidean algorithm, or Euclid's algorithm, is an efficient 
method for computing the greatest common divisor of two integers, the largest 
number that divides them both without a remainder.
Source: https://en.wikipedia.org/wiki/Euclidean_algorithm
"""
def euclid(x, y):
    if y == 0: return x
    a = max(x, y)
    b = min(x, y)

    while b != 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a
            
    
if __name__ == '__main__':
    print(euclid(int(sys.argv[1]), int(sys.argv[2])))

import sys

def euclid(x, y):
    if y == 0: return x
    a = max(x, y)
    b = min(x, y)
    gcf = 0

    while b != 0:
        if a > b:
            a -= b
        else:
            b = b - a
    return a
            
    
if __name__ == '__main__':
    print(euclid(int(sys.argv[1]), int(sys.argv[2])))

def process(s):
    p = [0] * (len(s) + 1)
    
    for i in range(1, len(s) + 1):
        p[i] = p[i - 1] + (1 if s[i - 1] == 'T' else 0)
    
    return p

def count(p, start, end):
    return p[end] - p[start - 1]

def path():
    s = input("Treasure path (T for treasure, . for empty): ")
    n = int(input("Number of queries: "))
    
    prefix = process(s)
    
    print("Enter queries (start end):")
    for _ in range(n):
        start, end = map(int, input().split())
        print(count(prefix, start, end))

path()
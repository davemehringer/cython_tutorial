def test(x):
    y = 0
    for i in range(x):
        y += i
    return y

def test1(x: int) -> int:
    y: int = 0
    i: int 
    for i in range(x):
        y += i
    return y
    

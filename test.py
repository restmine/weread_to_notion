def test(i):
    if i > 10:
        return (10,11)
    return (None,None)

if __name__ == "__main__":
    a,b = test(12)
    if a and b:
        print(a)


def numberToBinary(number):
    x=[]
    a="{0:b}".format(number)
    return a
    for j in a:
        x.append(int(j))
    for j in range(len(x),5):
        x.insert(0,0)
    return x

print(numberToBinary(5))

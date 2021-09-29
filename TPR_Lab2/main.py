with open('data') as f:
    w = f.readline()
    list = [float(x) for x in w.split()]


def BO(x, y, z, k, a):
    return ((x*y+z*k)*4-a)

def MO(x, y, z, k, a):
    return ((x*y+z*k)*4-a)

def B(x, y, z, k, a):
    return ((x*y+z*k)*5-a)

def M(x, y, z, k, a):
    return ((x*y+z*k)*5-a)

def O(x, y, z):
    return ((x+y*0*1+z*0*1))


print('Дохід великого підприємства після періоду очікування: ', BO(list[1], list[12], list[3],list[13], list[0]))
print('Дохід малого підприємства після періоду очікування: ',MO(list[6], list[12], list[8],list[13], list[5]))
print('Дохід великого підприємства: ', B(list[1], list[2], list[3],list[4], list[0]))
print('Дохід малого підприємства: ', M(list[6], list[7], list[8],list[9], list[5]))
bo = BO(list[1], list[12], list[3],list[13], list[0])
mo = MO(list[6], list[12], list[8],list[13], list[5])
b = B(list[1], list[2], list[3],list[4], list[0])
m = M(list[6], list[7], list[8],list[9], list[5])
print('Дохід малого підприємства після року очікування: ', O(mo, list[10], list[11]))
o = O(mo, list[10], list[11])

maximum = max(bo, mo, b, m)
if (maximum == bo):
    print('Отже, оптимальним рішенням є будівництво великого заводу із очікуванням у рік, тоді дохід становитиме - ', maximum)
elif(maximum == mo):
    print('Отже, оптимальним рішенням є будівництво малого заводу із очікуванням у рік, тоді дохід становитиме - ', maximum)
elif(maximum == b):
    print('Отже, оптимальним рішенням є будівництво великого заводу без очікування, тоді дохід становитиме - ', maximum)
elif(maximum == o):
    print('Отже, оптимальним рішенням є будівництво малого заводу без очікування, тоді дохід становитиме - ', maximum)
else:
    print('Отже, оптимальним рішенням є будівництво малого заводу підприємства після року очікування, тоді дохід становитиме - ', maximum)
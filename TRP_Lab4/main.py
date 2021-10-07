import numpy as np
f = open('data', encoding='utf-8', mode='r')
file = open('data_par', encoding='utf-8', mode='r')
data = []
param = []

for line in f:
    data.append(line.replace('\n','').split(", "))

for line in file:
    param.append(line.replace('\n','').split(", "))
ratings =[]
value = [0.25, 0.25, 0.15, 0.2, 0.15]
result =[]
names = [ 'Чернівці',  'Бакота','Тернопіль','Турка']


for row in param:
    print("{: >0} {: >25} {: >10} {: >10} {: >10} {: >10} {: >10}".format(*row))

for row in data:
    print("{: >0} {: >25} {: >10} {: >10} {: >10} {: >10} {: >10}".format(*row))

for element in data:
    element.pop(0)
    element.pop(0)
    element.pop(0)
    ratings.append(element)

ratings = np.array(ratings)
ratings = ratings.astype(float)
# ratings = ratings.transpose()

value = np.array(value)
value = value.astype(float)
value = value.transpose()

final_rat = [value[i] * ratings[i] for i in range(len(ratings))]
final_rat = np.array(final_rat)
final_rat = final_rat.transpose()

result.append(np.sum(value))
for element in final_rat:
    result.append(np.sum(element))


print('\nСума\t\t\t\t\t ', end="  ")
for element in result:
    print("\t\t%.2f" % round(element, 2), end=" ")
index = result.index(max(result))

print("\n\nСума найкращого рішення становить: %(maxvalue)f, це є   %(name)s " % {"maxvalue": max(result), "name":names[index-1]})

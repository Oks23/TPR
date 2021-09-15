with open('matrix', 'r') as my_matrix:
    matrix = [[int(num) for num in line.split(',')] for line in my_matrix]
print('\nОтримана матриця має наступний вигляд:', matrix, '\n\nКритерій Вальда:')

minValues = []
maxValues = []

for x in matrix:
    minValues.append(min(x))
    maxValues.append(max(x))

print(minValues, '\nТепер обираємо максимальне значення із мінімальних, отримуємо:', max(minValues))


print('\nМаксимальний критерій:\n', maxValues)
print('Тепер обираємо максимальне значення із максимальних, отримуємо:', max(maxValues))


koef = 0.7
print("\nКритерій Гурвіца з коефіцієнтом %(koef)s"%{"koef":"{:.1f}".format(koef)})
hurwitz = []
iterator = 0
for x, y in zip(minValues, maxValues):
    hurwitz.append(koef*x + (1-koef)*y)
    print("K(%(iterator)d) = %(hurwitz)d" % {"iterator": iterator, "hurwitz":hurwitz[iterator]})
    iterator +=1
print("Тепер обираємо максимальне значення із отриманих: %(max)d"%{"max":max(hurwitz)}, '\n')

print('Критерій Лапласа:')
lmatrix = []
for x in matrix:
    lmatrix.append((sum(x)+0.0)/len(x))
print(lmatrix, '\nТепер обираємо максимальне значення із отриманих, маємо:', lmatrix[lmatrix.index(max(lmatrix))])


print('\nКритерій Байеса-Лапласа:\nМаємо ймовірності:')
pn = [.55, .3, .15]
print("p1 = %(p0)s p2 = %(p1)s p3 = %(p2)s"%{"p0":"{:.2f}".format(pn[0]), "p1":"{:.2f}".format(pn[1]), "p2":"{:.2f}".format(pn[2])})

blmatrix = []
maxbl = []
for x in matrix :
    blmatrix.append([(i + .0) * y for i, y in zip(x, pn)])
    maxbl.append(sum([(i + .0) * y for i, y in zip(x, pn)]))

print('Отримані значення:\n', maxbl, "\nТепер обираємо максимальне значення із отриманих, маємо: %(max)s"%{"max":max(maxbl)})

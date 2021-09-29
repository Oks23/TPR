import itertools

def compare(pair, list):
    sum1, sum2 = 0, 0
    for x in list:
        if x.order.index(pair[0]) < x.order.index(pair[1]):
            sum1 += x.count
        else:
            sum2 += x.count
    print(f'{pair[0]} : {sum1} vs {pair[1]} : {sum2}')
    return [pair[0], pair[1]] if sum1 > sum2 else [pair[1],pair[0]]


class Option():
    def __init__(self, order, count):
        self.order = order
        self.count = count


class Solver():

    def __init__(self, options, candidates):
        self.options = options
        self.candidates = candidates


    # метод Борда
    def bordMethod(self):
        candCount = len(self.candidates) - 1

        points = {x:sum([y.count * (candCount - y.order.index(x)) for y in self.options]) for x in self.candidates}
        print(f'Кандидати на виборах набрали наступні оголоси: ', points)
        bestCand = max(points, key = lambda item: points[item])
        print(f'\nКандидат, що виграв, за Методом Борда, є кандидат  {bestCand}, який набрав {points[bestCand]} голосів.\n')

    # метод Кондорсе
    def kondorceMethod(self):
        combinations = [x for x in itertools.combinations(self.candidates,2)]
        compared = [compare(pair, self.options) for pair in combinations]
        dominated = [x[0] for x in compared]
        print(f'А за методом Кондорсе у даних виборах виграє кандидат {max(set(dominated), key=dominated.count)}')



candidates = ["A","B","C"]
with open('data') as f:
    w = f.readlines()
    liste = [x.split() for x in w]


with open('votes') as f1:
    w1 = f1.readline()
    votes = [int(x) for x in w1.split()]

list = []
for x in range(len(liste)):
    list.append(Option(liste[x], votes[x]))

solver = Solver(list, candidates)
solver.bordMethod()
solver.kondorceMethod()

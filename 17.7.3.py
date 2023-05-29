per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму '))
def depos (a):
    return int(a*money/100) #функция вычисления накопленных средств
deposit = list(map(depos, dict.values(per_cent))) #накопленные средства за год вклада в каждом из банков
print ("deposit = ", deposit, "\nМаксимальная сумма, которую вы можете заработать — ", max(deposit))

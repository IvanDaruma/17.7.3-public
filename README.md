# 17.7.3-public
Онлайн-школа SkillFactory, курс Тестировщик-автоматизатор на Python (QAP), Модуль 17 (Основы Python. Типы данных) 
Задание 17.7.3
Вам дан словарь per_cent с распределением процентных ставок по вкладам в различных банках таким образом, что ключ
— название банка, значение — процент. Напишите программу, в результате которой будет сформирован список deposit
значений — накопленные средства за год вклада в каждом из банков. На вход программы с клавиатуры вводится сумма
money, которую человек планирует положить под проценты. Добавьте в программу поиск максимального значения и его
вывод на экран в формате: "Максимальная сумма, которую вы можете заработать — deposit[i]", где вместо deposit[i]
будет выведено максимальное значение списка.

Реализовал через объявление отдельной функции вычисления начисленных процентов (в модуле этого материала
не было, изучил сам) и использование функции map.

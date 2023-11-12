import random

# Ввод
m = int(input('Введите число экспериментов >=1 и <=1000 '))
n = int(input('Введите число испытаний >=100 и <=2000 '))

sum_n = 0
k1 = []
k2 = []
k3 = []

# Цикл по номеру эксперимента
for j in range(m):
    kol = 0
    # Цикл по номеру испытания
    for i in range(n):
        k1.append(random.random())
        k2.append(random.random())
        k3.append(random.random())
        if k1[i] < 0.1 or (k2[i] < 0.1 and k3[i] < 0.1):
            kol += 1
    p = kol / n
    print('Вероятность отказа системы = ' + str(p))
    sum_n += p
    k1.clear()
    k2.clear()
    k3.clear()

sred = sum_n / m
print('Среднее значение вероятности отказа системы = ' + str(sred))
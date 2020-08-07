while True:
    age = input('Введите возраст (полных лет цифрой): ')
    if age.isdigit():
        age = int(age)
        break
    else:
        print('Надо ввести число!')

while True:
    gender = input('Введите пол (М/Ж): ')
    gender = gender.upper()
    if gender == 'М' or gender == 'Ж':
        break
    else:
        print('Введите информацию в корректном формате.')

while True:
    age_expected = input('Введите ожидаемую продолжительность жизни (полных лет цифрой): ')
    if age_expected.isdigit():
        age_expected = int(age_expected)
        break
    else:
        print('Надо ввести число!')

if gender == 'М':
    years_left = 65 - age
else:
    years_left = 60 - age
print(f'Осталось лет до пенсии: {years_left}')

if gender == 'М':
    years_live = age_expected - 65
else:
    years_live = age_expected - 60
print(f'Ожидаемый период дожития: {years_live}')

inflation = [160.4, 2508.85, 839.87, 215.02, 131.33, 21.81, 11.03, 84.44, 36.56, 20.2, 18.58, 15.06, 11.99, 11.74,
             10.91, 9,
             11.87, 13.28, 8.8, 8.78, 6.1, 6.58, 6.45, 11.36, 12.91, 5.38, 2.52, 4.27, 3.05]

inflation = list(reversed(inflation))

if not years_left:
    i = 0
elif years_left >= 29:
    i = float(sum(inflation) / 29)
else:
    i = float(sum(inflation[:years_left]) / years_left / 100)

print(f'Ожидаемая средняя инфляция {round(i * 100, 2)}%')

while True:
    savings = input('Введите сумму, которую Вы готовы откладывать ежегодно (в тыс. рублей, необходимо ввести число): ')
    if savings.isdigit():
        savings = int(savings)
        break
    else:
        print('Надо ввести число!')

while True:
    rate = input('Вы можете задать норму доходности в процентах или определить как отношение к уровню инфляции. '
                 'Введите ожидаемую норму доходности в процентах (необходимо ввести число): ')
    if rate.isdigit():
        rate = float(rate) / 100
        break
    if not rate:
        rate = input('Введите ожидаемую норму доходности в процентах от инфляции (необходимо ввести число): ')
        if rate.isdigit():
            rate = i * float(rate) / 100
            print(f'Ожидаемая средняя норма годовой доходности {round((rate * 100), 2)} %')
            break
    print('Надо ввести число!')

while True:
    current_savings = input('Введите сумму текущих сбережений (в тыс. рублей, необходимо ввести число): ')
    if current_savings.isdigit():
        current_savings = float(current_savings)
        break
    else:
        print('Надо ввести число!')

total_savings = current_savings
for year in range(years_left + 1):
    total_savings = total_savings * (1 + rate) + savings

print(f'Итоговая сумма пенсионных сбережений: {int(total_savings)} тыс. рублей.')

real_savings = current_savings
for year in range(years_left + 1):
    real_savings = real_savings * (1 + (rate - i)) + savings

print(f'Сумма реальных сбережений {int(real_savings)} тыс. руб.')

rate = rate / 2  # Предполагается снижение нормы доходности вдвое в пенсионный период

monthly = (total_savings * (rate / 12)) / (1 - 1 / (1 + (rate / 12)) ** (years_live * 12))

print(f'Размер Вашей пенсии составит {round(monthly, 2)} тыс. рублей.')

monthly_real = (real_savings * (rate / 12 - i / 12)) / (1 - 1 / (1 + (rate / 12 - i / 12)) ** (years_live * 12))

print(f'Реальный размер Вашей пенсии составит {round(monthly_real, 2)} тыс. рублей.')
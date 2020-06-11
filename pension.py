while True:
    age = input('Введите возраст (полных лет цифрой): ')
    if age.isdigit() == True:
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
    if age_expected.isdigit() == True:
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

inflation = [160.4, 2508.85, 839.87, 215.02, 131.33, 21.81, 11.03, 84.44, 36.56, 20.2, 18.58, 15.06, 11.99, 11.74, 10.91, 9,
11.87, 13.28, 8.8, 8.78, 6.1, 6.58, 6.45, 11.36, 12.91, 5.38, 2.52, 4.27, 3.05]

inflation = list(reversed(inflation))

if not years_left:
    i = 0
elif years_left >= 29:
    i = round(sum(inflation) / 29, 2)
else:
    i = round(sum(inflation[:years_left]) / years_left, 2)

print(f'Ожидаемая средняя инфляция {i}%')

while True:
    savings = input('Введите сумму, которую Вы готовы откладывать ежегодно (в тыс. рублей, необходимо ввести число): ')
    if savings.isdigit():
        savings = int(savings)
        break

while True:
    rate = input('Введите ожидаемую норму доходности в процентах от инфляции (необходимо ввести число: ')
    if rate.isdigit():
        rate = round((i / 100) * (int(rate) / 100), 2)
        break

print(f'Ожидаемая средняя норма годовой доходности {rate * 100} %')





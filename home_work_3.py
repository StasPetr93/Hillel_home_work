# Улучшений калькулятор

print('Чтобы завершить оперцию, введите в операторе  "="')
list_for_calc = []
while True:
    num = input('введите номер: ')
    try:
        num = float(num)
    except:
        print('Такой цифры не существует. Пререзапустите програму! ')
        break
    list_for_calc.append(str(num))
    action = input('Введите оператор: ')
    if action not in '+-*/=':
        print('Это не правильный оператор. Пререзапустите програму!')
        break
    if action == '=':
        print('Результат ', eval(''.join(list_for_calc)))
        break
    list_for_calc.append(action)


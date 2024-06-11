# 1 Создаём переменную с кортежем из элементов разных типов данных и выводим на экран

immutable_var = (1, 2, 'foxtrot', 3.5, False)
print('Кортеж: ' + str(immutable_var))

# 2 Такой кортеж изменить нельзя, так как кортеж неизменяемый объект, чтобы иметь возможность его изменять необходимо включить в состав кортежа список, например:
immutable_var = (1, 2, ['foxtrot', 'tango', 'bravo'], 3.5, False)
print('\nКортеж со списком внутри: ' + str(immutable_var))
immutable_var [2][0] = 'echo'
immutable_var [2][1] = 'yankee'
immutable_var [2][2] = 'zulu'
print('\nКортеж с изменениями: ' + str(immutable_var))

# 3 Создаём переменную со списком из нескольких элементов и изменяем их
mutable_list = ['kilo', 'delta', 'charlie', 2, 3, 0.25]
print('\n\n\n\nСписок: ' + str(mutable_list))
mutable_list.append('mil.std_4')
print('\nИзмененный вариант списка с добавлением элемента в конце: ' + str(mutable_list))
mutable_list.remove('kilo')
mutable_list.extend('radio')
print('\nИзмененный вариант списка с удалением первого элемента и добавлением через extend новых: ' + str(mutable_list))


print('___Calc___')
print('1-додавання:')
print('2-віднімання:')
print('3-множення:')
print('4-ділення:')
vybir1 = float(input('Зробіть свій вибір'))
if vybir1 == 1:
	num1 = float(input('Введіть перше число:   '))
	num2 = float(input('Введіть друге число:   '))
	dod = num1 + num2
	print("Сума двох чисел:  " + str(dod))
elif vybir1 == 2:
	num1 = float(input('Введіть перше число:   '))
	num2 = float(input('Введіть друге число:   '))
	dod = num1 - num2
	print("Різниця двох чисел:  " + str(dod))
elif vybir1 == 3:
	num1 = float(input('Введіть перше число:   '))
	num2 = float(input('Введіть друге число:   '))
	dod = num1 * num2
	print("Добуток двох чисел:  " + str(dod))
elif vybir1 == 4:
	num1 = float(input('Введіть перше число:   '))
	num2 = float(input('Введіть друге число:   '))
	dod = num1 / num2
	print("Різниця  двох чисел:  " + str(dod))





















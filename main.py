from num2words import num2words

lang = 'pt-br'

try:
	num = int(input('Number >> '))
except:
	print("The value entered is not a number")
	exit()

num2 = num2words(num, lang=lang)
num3 = num2words(num, lang=lang, to='ordinal')

print('full number: 'num2)
print('ordinal: '+num3)

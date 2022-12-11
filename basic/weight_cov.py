weight = int(input("Weight : "))
unit = input("(L)bs or (K)g : ")

output = 0

if unit.upper() == 'L':
	output = weight * 0.454
elif unit.upper() == 'K':
	output = weight * 2.205
else :
	print('INVALID VALUE')
	exit()

print(f'Converted Weight : {output}')
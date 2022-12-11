is_hot = False
is_cold = True

if is_hot and not is_cold:
	answer = " It's a hot day \n Stay Hydrated"
elif is_cold and not is_hot:
	answer = " It's a cold day \n Wear warm clothes"
else:
	answer = " It's a lovely day"

print(f'\n{answer}\n Enjoy Your Day \n')
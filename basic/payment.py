price = 1000000

has_good_credit = True

if has_good_credit:
    down_price = price * 0.1
else:
    down_price = price * 0.2

print(f'Down Payment = ${down_price}')
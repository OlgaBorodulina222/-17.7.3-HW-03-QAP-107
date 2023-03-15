per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int( input("Введите сумму вклада"))
deposit = []
for key in per_cent:
    deposit.append(int(money*per_cent[key]))

print(f'deposit={deposit}')
max_deposit=max(deposit)
print(f'Максимальная сумма, которую вы можете заработать - {max_deposit}')




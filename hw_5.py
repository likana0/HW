print('Привет! Сегодня я буду твоим личным бухгалтером!')

user_profit = int(input('Введи прибыль за этот месяц в рублях - '))
user_costs = int(input('А теперь введи сумму издержек за этот месяц в рублях - '))

if user_profit > user_costs:
    profit = user_profit - user_costs
    ratio = (profit / user_profit) * 100
    print(f'В этом месяце твоя чистая прибыль составила - {profit}р')
    print(f'Рентабельность выручки - {ratio}%')

    user_personal = int(input('Введи количество сотрудников - '))
    personal = user_profit / user_personal
    print(f'На 1 сотрудника приходится прибыли - {personal}р')

else:
    cost = user_costs - user_profit
    print(f'К сожалению, в этом месяце твои издержки превысили доходы на - {cost}р')



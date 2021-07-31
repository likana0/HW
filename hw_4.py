user_number = int(input('Введи любое целое и положительное число - '))
un = -1

while user_number > 10:
    m_number = user_number % 10
    user_number //= 10
    if m_number >= un:
        un = m_number

print(f'Самое большое число в твоем - {un}')
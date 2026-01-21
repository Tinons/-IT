money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0
capital = money_capital
current_spend = spend

while capital + salary >= current_spend:
    capital = capital + salary - current_spend
    months += 1
    current_spend *= (1 + increase)  # со следующего месяца расходы больше

print("Количество месяцев, которое можно протянуть без долгов:", months)

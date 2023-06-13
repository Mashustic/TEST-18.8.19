# запрос у пользователя кол-ва билетов
n_tickets=int(input("Сколько билетов Вы хотите приобрести?Если приобретаете более трёх билетов, "
                    "получаете скидку 10% на весь заказ:"))

cost1 = 0
cost2 = 990
cost3 = 1390
s_tickets=0 # переменная, куда суммируется стоимость билетов

for age in range (n_tickets):
    age = int(input("Введите возраст посетителя:"))
    if age<18:
     s_tickets=s_tickets+cost1
     print(" цена билета для Вас:", cost1)
     print ("общая стоимость билетов для Вас", s_tickets)
    elif  18 <= age <= 25:
     s_tickets=s_tickets+cost2
     print(" цена билета для Вас:", cost2)
     print("общая стоимость билетов для Вас", s_tickets)
    elif age >=25:
     s_tickets = s_tickets + cost3
     print(" цена билета для Вас:", cost3)
     print("общая стоимость билетов для Вас", s_tickets)


if n_tickets > 3:
    s_tickets=s_tickets*0.9
    print("Ваши билеты со скидкой 10% будут стоить:", s_tickets)
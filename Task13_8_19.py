def checkAndGetNumber(text):
    success = False
    n = 0
    while not success:
        try:
            # Пытаемся поймать исключение от int(string_nr)
            string_nr = input(text)
            n = int(string_nr)
            if n > 0:
                # Проверяем что больше нуля и если все норм, выходим из цикла
                success = True
            else:
                print("Значение должно быть больше нуля")
        except ValueError:
            # Ловим исключение и печатаем текст
            print("Нужно вводить только цифры, повторите попытку")
    return n


count = checkAndGetNumber("Сколько мест вы хотите забронировать? ")

amount = 0

for i in range(count):
    age = checkAndGetNumber(f"Введите возраст участника номер {i + 1}: ")
    if age < 18:
        # Меньше 18, то пропускаем
        continue
    if age < 25:
        # 18 или меньше 25, не включая 25
        amount += 990
    else:
        amount += 1390

if count > 3:
    print("Применена скидка 10%")
    amount *= 0.9

print(f"Сумма к оплате: {amount}")

counter = 0

for ticket_num in range(0, 1000000):
    num6 = ticket_num % 10

    tmp = ticket_num // 10
    num5 = tmp % 10

    tmp = ticket_num // 10
    num4 = tmp % 10

    tmp = tmp // 10
    num3 = tmp % 10

    tmp = tmp // 10
    num2 = tmp % 10

    tmp = tmp // 10
    num1 = tmp % 10

    if num1+num2+num3 == num4+num5+num6:
        counter = counter + 1
        print(num1,num2, num3, num4, num5, num6)

print()
print(counter)



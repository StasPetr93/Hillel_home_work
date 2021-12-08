#ford = ['mondeo', 'focus', 'kuga']
#fiat = ['tipo', 'panda', '500']
#renault = ['clio', 'megan', 'duster']

print('Введите модель авто и на выходе получите марку, если хотите прекратить поиск пропишите: "exit"')
print()
ford = ['mondeo', 'focus', 'kuga']
fiat = ['tipo', 'panda', '500']
renault = ['clio', 'megan', 'duster']


while True:
    model = input("Введите модель авто: ")
    if model in ford:
        print("ford")
    elif model in fiat:
        print("fiat")
    elif model in renault:
        print("renault")
    else:
        print('error')
        if model == "exit":
            break

end_1 = input("До свидания !!!")
a = input()
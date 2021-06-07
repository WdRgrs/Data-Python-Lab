open_file = open("CupcakeInvoices.csv")

for line in open_file: 
    print(line)
    break

for cup in open_file:
    value = cup.split(',')
    print(value[2])
    break

total = 0
ans = 0

for amount in open_file:
    value = amount.split(',')
    ans = int(value[3]) * float(value[4])
    print(round(ans, 2))
    break

for amount in open_file:
    value = amount.split(',')
    total = total + int(value[3]) * float(value[4])
    break



for type in open_file:
    value = type.split(',')
    if value[2] == 'Strawberry':
            ans = int(value[3]) * float(value[4])
            print(round(ans, 2))
            total = total + ans
            break

for type in open_file:
    value = type.split(',')
    if value[2] == 'Vanilla':
            ans = int(value[3]) * float(value[4])
            print(round(ans, 2))
            total = total + ans
            break

for type in open_file:
    value = type.split(',')
    if value[2] == 'Chocolate':
            ans = int(value[3]) * float(value[4])
            print(round(ans, 2))
            total = total + ans
            break

x = round(total, 2)
print(x)

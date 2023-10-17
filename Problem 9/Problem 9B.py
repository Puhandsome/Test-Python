list_price = input().split()
list_quantity = input().split()
sum = 0
for i in range(len(list_price)):
    x = float(list_price[i])*float(list_quantity[i])
    sum += x
print(round(sum,2))
print("Welcome to Apple Store")
a = str(input("Hello, how can I contact you?(ENTER YOUR NAME IN LETTERS!!!)"))
print(a,",view our catalog!")


order = []
print("Catalog, Apple Store:")
Iphone = "Айфон 15 про макс"
price_1 = 1000
print(Iphone)
price_2 = 1700
Macbook ="Макбук про м3"
print(Macbook)
price_3 = 690
Ipad = "Айпад рпо"
print(Ipad)
Airpods ="Аирподс про 3"
price_4 = 500
print(Airpods)
apple = str(input("enter technique"))
try:
    apple = str(input("enter technique"))
except ValueError:
    print("there is no such")
    price_5 = 0
if apple == Iphone:
    order.append(Iphone)
    print(order)
    price_5 += price_1
elif apple == Macbook:
    order.append(Macbook)
    print(order)
    price_5 += price_2
elif apple == Airpods:
    order.append(Airpods)
    print(order)
    price_5 += price_4
elif apple == Ipad:
    order.append(Ipad)
    print(order)
    price_5 += price_3
    payment = str(input("payment(card,cash)"))
try:    payment = str(input("payment(card,cash)"))
except ValueError:
    print("no such payment *****")
price = int(input("enter price"))
try:
    price = int(input("enter price"))
except ValueError:
    print("we don't accept ***** like that")
    change =- price_5 - price
print("your order in path")
print("Thank f o r you  your purchase, come back to my Apple Store. Tim Cook")
print(a,",Good bay")







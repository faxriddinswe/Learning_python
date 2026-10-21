# Task 1

order_total = 85000
product_available = True
inside_city = False


if order_total < 0:
    print("Buyurtma qiymati 0 dan katta bo'lishi kerak ")

elif product_available == False:
    print("Rad etildi ")


elif order_total == 100000 or order_total > 100000:
    print("yetkazib berish bepul")

elif inside_city == True:
    print(" 15000 ming so'm yetkazish ")

elif inside_city == False:
    print(" Yetkazib berish 25000 so'm ")


print(f"Buyurtma qabul qilindi")

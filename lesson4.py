# # Bankomatdan pul yechish 

# balance = 500000
# amount = 175000

# if amount <= 0:
#     print("Pul yechish to'xtatildi: Summa musbat bo'lishi kerak ")

# elif amount % 50000 != 0:
#     print("Pul yechish rad etildi: summa 50 000 so'mga karrali bo'lishi kerak")

# elif amount > balance:
#     print("Pul yechish rad etildi: hisobda yetarli mablag' mavjud emas")

# else:
#     print("Pul yechishga ruxsat"


# Task 3

# order_total = 120000
# is_inside_city = False

# if order_total < 0:
#     print("Xato: Buyurtma qiymati manfiy bo'lishi mumkin emas")

# if order_total < 30000:
#     print("Xato : Qabul qilinmaydi: 30000 dan kam summa")
# else:
#     print("Buyurtma qabul qilindi ")


# if order_total >= 200000:
#     delivery_fee = 0

# elif is_inside_city:
#     delivery_fee = 15000

# else:
#     delivery_fee = 30000

# total_amount = order_total + delivery_fee
    
# print(f"Yetkazib berish narxi: {delivery_fee} so'm")
# print(f"Jami: {total_amount} so'm")



# Task 4

score = 88
age = 18
interview_passed = True

if age < 16:
    print("Xato : Talabaning yoshi 18 dan kichik")

elif score < 0 or score > 100 :
    print("Xato : Talaba bali 0 va 100 orasida emas ")

elif score >= 85 and interview_passed:
    print("Stipendiya beriladi !")

elif score >= 70 and interview_passed:
    print("O'qishga qabul qilinadi")

else:
    print("rad etildi")


print(f"Natija : {score}")

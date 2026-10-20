# Bankomatdan pul yechish 

balance = 500000
amount = 175000

if amount <= 0:
    print("Pul yechish to'xtatildi: Summa musbat bo'lishi kerak ")

elif amount % 50000 != 0:
    print("Pul yechish rad etildi: summa 50 000 so'mga karrali bo'lishi kerak")

elif amount > balance:
    print("Pul yechish rad etildi: hisobda yetarli mablag' mavjud emas")

else:
    print("Pul yechishga ruxsat")


# Task 2


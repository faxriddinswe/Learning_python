# # Task 1

students = {
    "Ali": (90, 75),
    "Vali": (45, 80),
    "Malika": (85, 30),
    "Aziza": (70, 60)
}

for name, (attendance, score) in students.items():
    if not (0 <= attendance <= 100 and 0 <= score <= 100):
        print(f"{name}: Xato ma'lumot")
    elif attendance < 60:
        print(f"{name}: Imtihonga qo'yilmaydi")
    elif score < 40:
        print(f"{name}: Qayta topshiradi")
    else:
        print(f"{name}: O'tdi")



# Task 2

amount = 3500000
account_active = True
familiar_location = False

if amount < 0:
    print("Tolov rad etildi: notogri summa")
elif not account_active:
    print("Tolov rad etildi: hisob faol emas")
elif amount > 10000000:
    print("Tolov qolda tekshirishga yuborildi")
elif amount > 2000000 and not familiar_location:
    print("Tolov qolda tekshirishga yuborildi")
else:
    print("Tolov tasdiqlandi")



# Task 3

rooms = {
    "A xona": {
        "capacity": 5,
        "available_times": {"09:00", "10:00", "14:00"}
    },
    "B xona": {
        "capacity": 12,
        "available_times": {"10:00", "11:00", "14:00"}
    },
    "C xona": {
        "capacity": 30,
        "available_times": {"09:00", "11:00"}
    }
}

participants = 10
requested_time = "10:00"
is_internal = True

if not is_internal and participants < 5:
    print("Tashqi yigilish uchun ishtirokchilar soni kamida 5 ta bo‘lishi kerak")
elif participants < 1:
    print("Ishtirokchilar soni kamida 1 bolishi kerak")
else:
    best_room = None
    min_capacity = float('inf')
    
    for room_name, info in rooms.items():
        if info["capacity"] >= participants and requested_time in info["available_times"]:
            if info["capacity"] < min_capacity:
                min_capacity = info["capacity"]
                best_room = room_name
                
    if best_room:
        print(f"{best_room} tanlandi")
    else:
        print("Mos xona mavjud emas")



# Task 4

available_spaces = 4
payment_completed = True
is_electric = True
special_spaces_available = True

if available_spaces < 0:
    print("Tizim malumot xatosi: bosh joylar soni manfiy bolishi mumkin emas")
elif available_spaces == 0:
    print("Kirish taqiqlandi: bosh joylar mavjud emas")
elif not payment_completed:
    print("Kirish taqiqlandi: tolov qilinmagan")
else:
    print("Kirishga ruxsat berildi")
    if is_electric and special_spaces_available:
        print("Elektr avtomobili uchun maxsus joyga yonaltirildi")
    else:
        print("Oddiy joyga yonaltirildi")

# Task 5

weight = 24
courier_busy = False
can_carry_heavy = True
serves_outside_city = True
outside_city = True

# Shartlarni tekshirish
if weight <= 0:
    print("Buyurtma rad etildi: og‘irlik 0 dan katta bo‘lishi kerak")
elif courier_busy:
    print("Buyurtma rad etildi: kuryer band")
elif weight > 20 and not can_carry_heavy:
    print("Buyurtma rad etildi: kuryer og‘ir yukni ko‘tara olmaydi")
elif outside_city and not serves_outside_city:
    print("Buyurtma rad etildi: kuryer shahar tashqarisiga xizmat ko‘rsatmaydi")
else:
    print("Buyurtma kuryerga biriktirildi")
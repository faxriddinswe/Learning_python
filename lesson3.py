#  Task 1

ticket_ids = [101, 203, 101, 305, 203, 101, 410]
sanoq = {}

for id in ticket_ids:
    if id in sanoq:
        sanoq[id] += 1
    else:
        sanoq[id] = 1

for id, marta in sanoq.items():
    if marta > 1:
        print(f"{id}, {marta} marta ishtirok etgan")


# Task 2











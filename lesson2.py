# task 1 

# nums = [4, 9, 2, 15, 7]

# max_qiymat = nums[0]
# max_indeks = 0

# for indeks, qiymat in enumerate(nums):
#     if qiymat > max_qiymat:
#         max_qiymat = qiymat
#         max_indeks = indeks

# print(f"Eng katta son: {max_qiymat}")
# print(f"Indeksi: {max_indeks}")

# task 2

nums = [1, 2, 3, 34, 4, 5]

juft_sonlar = []
toq_sonlar = []

for son in nums:
    if son % 2 == 0:
        juft_sonlar.append(son)   
    else:
        toq_sonlar.append(son)    

print(f"Juft sonlar: {juft_sonlar}")
print(f"Toq sonlar: {toq_sonlar}")


# task 3

nums = [3, -1, 0, -7, 5]

for i in range(len(nums)):
    if nums[i] < 0:
        nums[i] = 0

print(nums)


# task 4

words = ["anor", "uzum", "ananas", "shaftoli"]
N = 4
results = []

for i in range(len(words)):
        
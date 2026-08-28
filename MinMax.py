# min dan max
# jangan pakai .min() dan .max()

numbers = [4, 7, 2, 9, 1, 7, 4, 10, 2]
terbesar = numbers[0]
terkecil = numbers[0]

for i in numbers:
    if i > terbesar:
        terbesar = i 
print("Angka terbesar :",terbesar)

for i in numbers:
    if i < terkecil:
        terkecil = i 
print("Angka terkecil :",terkecil)
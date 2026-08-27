# Input: 10
# Output: Positif
# Input: -5
# Output: Negatif

#Positif
number = int(input("Masukkan nomor untuk mengetahui angkanya: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
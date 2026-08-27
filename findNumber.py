numbers = [1, 2, 3, 5, 6, 7, 8]

def find_missing(numbers):
    for i in range(1, max(numbers) + 1):

        if i not in numbers:
            return i


print("Angka yang hilang:", find_missing(numbers))
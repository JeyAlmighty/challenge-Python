#1. Minimal 8 karakter
#2. Memiliki angka
#3. Memiliki huruf besar

#Password: Python123
#Output: Password valid

#Password: python123
#Output: Password tidak valid

def validate_password(password):

    has_number = False
    has_upper = False

    # cek setiap karakter di sini
    for char in password:
        if char.isdigit():
           has_number = True
        if char.isupper():
            has_upper = True   

    # cek semua syarat di sini
    if len(password) >= 8 and has_upper and has_number:
        print("Password valid")
    else:
        print("Password tidak valid")


password = input("Masukkan password: ")

validate_password(password)
# Buat program perhitungan berat badan
# Gunakan konsep error handling
# Satuan berat KG



def timbangan():
    lbs = 2.20462

    while True:
        pilihan = input(
            "\nPilih menu:\n"
            "K = Kilogram\n"
            "L = Pound\n"
            "Q = Keluar\n"
            "Pilihan: "
        ).casefold()

        if pilihan == "q":
            print("Kamu keluar!")
            break

        elif pilihan == "k":
            try:
                berat = float(input("Masukkan berat badan dalam KG: "))
                print(f"Berat anda adalah {berat} Kilogram")

            except ValueError:
                print("Masukkan angka yang valid!")

        elif pilihan == "l":
            try:
                berat = float(input("Masukkan berat badan dalam KG: "))
                print(f"Berat anda adalah {berat * lbs:.2f} Pound")

            except ValueError:
                print("Masukkan angka yang valid!")

        else:
            print("Pilihan tidak valid!")


timbangan()
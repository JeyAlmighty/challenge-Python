# Angka pertama: 10
# Operator: /
# Angka kedua: 2
# Hasil: 5

def calculator():

    try:
        num1 = float(input("Angka pertama: "))
        operator = input("Operator: ")
        num2 = float(input("Angka kedua: "))

        if operator == "+":
            print("hasil dari ",num1," + ", num2," = ",num1 + num2)
        elif operator == "-":
            print("hasil dari ",num1," - ", num2," = ",num1 - num2)    
        elif operator == "*":
            print("hasil dari ",num1," * ", num2," = ",num1 * num2)    
        elif operator == "/":  
            print("hasil dari ",num1," / ", num2," = ",num1 / num2) 
        else:
            print("Operator tidak valid")

    except ZeroDivisionError:
        print("Tidak bisa membagi dengan nol")

    except ValueError:
        print("Input tidak valid")    


calculator()
# buatlah satu sampai seratus
# disetiap kelipatan 3 jadikan "fizz"
# disetiap kelipatan 5 jadikan "buzz"
# disetiap kelipatan 3 dan 5 jadikan "fizzbuzz"
 

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        i = "fizzbuzz"
        print(i)
    elif i % 3 == 0:
        i = "fizz"
        print(i)
    elif i % 5 == 0:
        i = "buzz"
        print(i)
    else:
        print(i)    
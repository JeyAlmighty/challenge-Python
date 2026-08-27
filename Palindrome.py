#Input: katak
#Output: Palindrome


def is_palindrome(text):

    if text == text[::-1] :
        print("Palindrome")
    else:
        print("Bukan palindrome")


text = input("Masukkan kata: ")

is_palindrome(text)
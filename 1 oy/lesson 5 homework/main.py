import random
# exercise 1
# text = "Elon Musk the richest person in the world"
#
# cut = text[0]
# extra = text[-1]
#
# print(cut, extra)

# Exercise 2
# text = input("Matni kiriting ").lower()
# # txt = "Uzbekistan one of the most beautiful place in the area"
#
# print("salom" in text)

# Exercise 3
# usa = "The United States of America (USA), commonly known as the United States (U.S.)"
#
# last = usa[-6:]
#
# print(last)

# Exercise 4
# information = """
# Ismi:   Familiyasi:  Yoshi:
# {} {}   {}""".format(input('Ismingizni kiriting '), input("Familiya"), input("Yosh "))

# information = "\nName: {} \nSurname: {} \nAge: {}\n You're succesfully log in your id {}".format(input("Your name "), input("Your surname "), input("Enter your age "), random.randrange(500, 1000))
#
#
# print(information)


# Exercise 5
# text = "Aka bugun ishdan kech keldi".lower()
#
# print("aka" in text, "amma")

# txt = "Uzbekistan one of the most beautiful place in the area"
#
# print(txt.split())


# Execrise 1
# a = input("ASCII ni belgisini kiriting ")
#
# print(ord(a))

# Exercise 2
# n = int(input("Butun son kiriting "))
#
# if n > 32 and n <= 126:
#     print(chr(n))
# else:
#     print("false")


# Exercise 3
# item = input("Son kiriting ")
#
# if len(item) == 1:
#     print(f"{chr(ord(item)-1)} : {item} : {chr(ord(item)+1)}")
# else:
#     print("Berilgan belgi bittadan kop!")

# Exercise 4
# n = int(input("Sonni kiriting "))
#
# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# if n >= 1 and n <= 26:
#     print(alphabet[n])
# else:
#     print("Xato son kiritingiz 26 dan oshmaydigan va 0 bolmagan son kiritib koring")


# Exercise 5
# numb = int(input("Son kiriting "))
#
# alphabet1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# alphabet1.sort(reverse=True)
#
# if numb >= 1 and numb <= 26:
#     print(alphabet1[numb])
# else:
#     print(False)

# Exercise 6
# txt = input("Belgini kiriting ")
#
# if txt.isnumeric():
#     print("Digit")
# else:
#     print("Lotin")

# Exercise 7
# text = list(input("Gap kiriting "))
#
# a = text[0]
# b = text[-1]
#
# print(a, b)
#
# print(ord(a), ord(b), sep ="\n")

# Exercise 8
# numb = int(input("Raqam hosil qiling "))
#
# text = ""
#
# for i in range(numb):
#     text += "A\n"
#
# print(text)

# Exercise 9
# txt = input("Birinchi gapni kiriting ")
#
# txt1 = input("2 - satrni kiriting ")
#
# a = txt +" "+ txt1
#
# print(a)

# Execise 10
# text = input("Matn kiriting ")
#
# a = text[::-1]
#
# print(a)

# Execise 11

# txt = input("Matni kiriting ")
#
# print(txt.split(" "))
#coding: utf-8

msg = input("Como te llamas: ")
print("Hola " + msg)

age = input("Cuantos años tienes?: ")
age = int(age)
if age <= 35:
    print("Estas hecho un mozo.")
else:
    print("Eres un viejales.")
print("Tienes " + str(age) + " años.")

number = input("Dime un número y te digo si es par: ")
number = int(number)
if number % 2 == 0:
    print("El número " + str(number) + " es par.")
else:
    print("El número no es par.")

print("\nWHILE\n")

current_number = 1
#Si da error poner 4 espacios
while current_number <= 10:
    print(current_number)
    current_number += 1

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
#Coge el último
print(unconfirmed_users.pop())
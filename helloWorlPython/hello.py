#coding: utf8
print("Variables y arrays")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
#for
print("\nFOR\n")

for value in my_foods:
    print(value.title())
print("Solo los dos últimos.")
for value in my_foods[1:3]:
    print(value.title())

print("\nIF\n")
age = 35

if age <= 35:
    print("Estas hecho un chaval.")
elif age > 35:
    print("Eres algo viejo.")
elif age > 70:
    print("Eres viejo del todo.")

if 'pizza' in my_foods:
    print("Tenemos pizza")

print("\nDICCIONARIOS")

alien_0 = {"color": "negro", "vida": 5, "points": 3}
print(alien_0["color"])
print(alien_0["vida"])
new_points = alien_0["points"]
print("Has recibido " + str(new_points) + " puntos.")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
del alien_0["points"]
print(alien_0)

user_0 = {
    "nombre": "Alberto",
    "primer_apellido": "Diéguez",
    "segundo_apellido": "Álvarez",
}
print(user_0)
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

if "points" not in alien_0:
    print("No tiene puntos.")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(name.title() + " Gracias por participar.")

print("\nExisten los siguientes lenguajes.\n")

for language in set(favorite_languages.values()):
    print(language.title())

alien_1 = {'color': 'green', 'points': 5}
alien_2 = {'color': 'yellow', 'points': 10}
alien_3 = {'color': 'red', 'points': 15}

aliens = [alien_1, alien_2, alien_3]
for alien in aliens:
    print(alien)
#Lista de un diccionario
pizza = {
    'pepperoni': 'fina',
    "ingredientes": ["tomate", "queso", "pepperoni"],
}

print("Has pedido una pizza " + pizza["pepperoni"] +
      " de pepperoni con los siguientes ingredientes: \n")
for ingrediente in pizza["ingredientes"]:
    print(ingrediente.title())

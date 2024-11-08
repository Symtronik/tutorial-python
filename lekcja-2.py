
x = 5 #int
y = 19.21 #float
z = "Jan" #str
a = True #bool

print(x)
print(y)
print(z)
print(a)

print(type(a))

name = "Adam"

myName = "Piotr"
MyName = "Rafał"
my_name = "Karol"

print(myName)
print(MyName)
print(my_name)

q, w, e = 4, "Pies", True

print(w)

i = o = p = "Kot"

print(o)

yourName = "Adam"
yourSurname = "Kowalski"

print("Imię: ",yourName, " Nazwisko: ", yourSurname)
print(yourName + " " + yourSurname)

def myfuncion():
    yourName = "Kasia"
    print("My name is:" , yourName)

myfuncion()

print(yourName)

# Zadanie 1
# Stwórz zmienną a o wartości 10 i zmienną b o wartości 3.
# Oblicz ich sumę, różnicę oraz iloczyn i przypisz do nowych zmiennych. Wypisz wyniki.

a = 10
b = 3
c = a + b
d = a - b
e = a * b

print("suma równa się: ", c)
print("różnica równa się: ", d)
print("iloczyn równa się:", e)

#Zadanie 2

# Zdefiniuj dwie zmienne dlugosc i szerokosc reprezentujące wymiary prostokąta.
# Oblicz pole i obwód prostokąta i wyświetl wyniki.

height = 8
width = 5
area = height * width
perimeter = 2 * (height + width)

print("Pole trójkata równa się:" , area)
print("Obwód trójkata równa się:", perimeter)
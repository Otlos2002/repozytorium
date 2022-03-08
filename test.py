
# Zad 1. Napisz skrypt, w którym tworzysz listę ulubionych sportów, odwróć ją a następnie dodaj mniej
# lubiane sporty na sam koniec.

# lista = ['kulturystyka', 'pilka_nozna', 'bieganie']
# print(lista)
# lista.reverse()
# print(lista)
# lista.append('siatkowka')
# lista.append('rzut kijem')
# print(lista)

# Zad 2. Stwórz słownik skrótów powszechnie używanych w gazetach lub artykułach internetowych.
# Jako klucz przyjmij skrót danego słowa, wartość to rozwinięcie tego skrótu.

# slownik = {'XD':'smiech',"omg":'o moj boze', 'lmao':'laugh my ass off' }
# print(slownik['XD'])
# print(slownik['omg'])
# print(slownik['lmao'])

# Zad 3. Stwórz słownik z ulubionymi grami komputerowymi. Pomyśl, co może być kluczem a co
# wartością w takim słowniku. Policz liczbę elementów w słowniku.

# slownik = {'w3':'wiedzmin 3 dziki gon',"lol":'league of legends', 'csgo':'counter strike global offensive' }
# print(len(dict.keys(slownik)))

# Zad 4. Napisz skrypt, który pobiera od użytkownika zdanie i liczy wystąpienia litery a. Użyj funkcji
# input

# napis = input("Podaj zdanie ")
# print(napis.count('a'))

# Zad 5. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: ab + c.
# Użyj instrukcji readline() i write()).

# import sys as system
# system.stdout.write("Podaj 3 liczby: ")
# a = system.stdin.readline()
# a=int(a)
# b = system.stdin.readline()
# b=int(b)
# c = system.stdin.readline()
# c=int(c)
# d = a*b + c
# d = str(d)
# system.stdout.write(d)

# Zad 6. Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich jest największa. W zależności od
# wyniku wyświetl odpowiedni komunikat. Użyj zagnieżdżeń.

# a = input('Podaj 3 liczby')
# b = input()
# c = input()
# a=int(a)
# b=int(b)
# c=int(c)
# print(max(a, b, c ))

# Zad 7. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float. Następnie za pomocą
# użycia pętli for podnieś każdą liczbę do kwadratu.

# lista = [ 1, 4, 6, 5, 3.14, 5.1, 6.5]
# for x in lista:
#     print(type(x))
# for x in lista:
#     print(x*x)

# Zad 8. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, następnie dodaje do listy tylko
# parzyste liczby.

# a=0
# lista = []
# while(a<10):
#     b=int(input("Podaj liczbe: "))
#     if(b%2==0):
#         lista.append(b)
#
#     a+=1
# print(lista)

# Zad. 9.
# Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika jeśli użytkownik poda
# wartość ujemną to powinien być wyłapany błąd.
# import math
# a = int(input('Podaj liczbe: '))
# if(a<0):
#     print('Blad!')
# else:
#     print(math.sqrt(a))






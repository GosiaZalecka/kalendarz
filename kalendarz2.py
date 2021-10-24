import calendar

#podanie roku
print("Czy to rok przestępny?")
year = input("podaj rok: ")

#sprawdzenie czy to rok przestępny
czy_przestępny = calendar.isleap(int(year))

if czy_przestępny == True:
    print("Tak, rok " + year + " to rok przestępny")
else:
    print("Nie, rok " + year + " to nie rok przestępny")
print("")

#podanie daty do sprawdzenia jaki to dzień tygodnia
print("Znasz datę i zastanawiasz się jaki dzień tygodnia to był?")
data_rok = int(input("wpisz rok: "))
data_miesiąc = int(input("wpisz miesiąc: "))
while data_miesiąc < 1 or data_miesiąc > 12:
    print("Przypominam, że rok ma 12 miesięcy")
    data_miesiąc = int(input("wpisz miesiąc: "))

krótkie_miesiące = (2, 4, 6, 9, 11)

data_dzień = int(input("wpisz dzień: "))
while data_dzień < 1 or data_dzień > 31:
    print("Miesiąc ma do 31 dni")
    data_dzień = int(input("wpisz dzień: "))

while data_miesiąc in krótkie_miesiące and data_dzień > 30:
    print("miesiąc " + str(data_miesiąc) + " ma mniej dni")
    data_dzień = int(input("wpisz dzień: "))

print("Data to: " + str(data_rok) + "." + str(data_miesiąc) + "." + str(data_dzień))
dzień_tygodnia = calendar.weekday(data_rok, data_miesiąc, data_dzień)

#prezentacja wyniku w postaci dnia tygodnia
if dzień_tygodnia == 0:
    print("Poniedziałek")
if dzień_tygodnia == 1:
    print("Wtorek")
if dzień_tygodnia == 2:
    print("Środa")
if dzień_tygodnia == 3:
    print("Czwartek")
if dzień_tygodnia == 4:
    print("Piątek")
if dzień_tygodnia == 5:
    print("Sobota")
if dzień_tygodnia == 6:
    print("Niedziela")
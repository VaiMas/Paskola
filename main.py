from Paskola import Paskola

listas =[]
paskola = Paskola(0, 0, 0)
while True:
    try:
        print()
        pasirinkimas = int(input(
            "Pasirinkite veiksmą:\n1 - įvesti paskolos duomenis,\n2 - parodyti paskolos informaciją\n3 - paskaičiuoti paskolos mokėjimo grafiką\n4 - baigti darbą\n"))
        if pasirinkimas == 1:
            suma = int(input("Įveskite paskolos sumą (eurais)\n"))
            terminas = int(input("Įveskite paskolos atidavimo terminą (mėnesiais)\n"))
            palukanos = int(input("Įveskite paskolos palūkanų procentą (pvz., 10)\n"))
            paskola = Paskola(suma, terminas, palukanos)
        elif pasirinkimas == 2:
            paskola.paskolos_informacija()
        elif pasirinkimas == 3:
            paskola.mokejimo_grafikas()
        elif pasirinkimas == 4:
            print("Programa baigta")
            break
    except:
        print("Neteisingas pasirinkimas")


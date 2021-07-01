data_list = ["Menuo ", "Dalis", "Likutis", 'Palukanos', 'Suma']
duomenys = []


class Paskola:
    def __init__(self, suma, terminas, palukanos):
        self.suma = suma
        self.terminas = terminas
        self.palukanos = palukanos
        self._bendros_palukanos = 0
        self._bendra_suma = 0

    def paskolos_informacija(self):
        print(f'Paskolos suma: {self.suma} euru, paskolos terinas: {self.terminas} '
              f'menesiu, palukanu norma: {self.palukanos}')
        if self._bendra_suma != 0:
            print(f'Bendra palūkanų suma: {self._bendros_palukanos:.2f} eurų')
            print(f'Bendra mokėtina suma: {self._bendra_suma:.2f} eurų')
        else:
            print("Bendra palūkanų suma ir bendra mokėtina suma bus atvaizduota tik paskaičiavimus mokėjimo grafiką")

    def mokejimo_grafikas(self):
        imokos_dydis = self.suma / self.terminas
        sumoketos_palukanos = 0
        sumoketa_suma = 0
        likutis = self.suma
        print(f'\nMėnuo''\t\t''Dalis''\t\t''Likutis''\t\t\t''Palūkanos''\t\t''Suma')
        for menuo in range(1, self.terminas + 1):
            menesio_palukanos = (likutis * self.palukanos) / 100 / 12
            likutis -= imokos_dydis
            moketina_suma = imokos_dydis + menesio_palukanos
            print(
                f'{menuo}\t\t{imokos_dydis:.2f}\t\t{likutis:.2f}\t\t\t{menesio_palukanos:.2f}\t\t\t{moketina_suma:.2f}')
            sumoketos_palukanos += menesio_palukanos
            sumoketa_suma += moketina_suma
            duomenys.append(f'{menuo},{imokos_dydis:.2f},{likutis:.2f},{menesio_palukanos:.2f},{moketina_suma:.2f}')
        duomenys.append(f'Bendra suma, {self.suma}, ,{sumoketos_palukanos:.2f},{sumoketa_suma:.2f}')
        print(f'Bendra suma: {self.suma:.2f}\t\t\t\t{sumoketos_palukanos:.2f}\t\t\t{sumoketa_suma:.2f}')
        self._bendros_palukanos = sumoketos_palukanos
        self._bendra_suma = sumoketa_suma

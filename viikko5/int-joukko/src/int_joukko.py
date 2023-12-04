KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:

    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti or KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko or OLETUSKASVATUS

        if not isinstance(self.kapasiteetti, int) or self.kapasiteetti < 0:
            raise ValueError("Väärä kapasiteetti")

        if not isinstance(self.kasvatuskoko, int) or self.kasvatuskoko < 0:
            # Selkeät error-messaget helpottaa
            raise ValueError("Väärä kasvatuskoko")

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):

        if not self.kuuluu(n):

            if self.alkioiden_lkm == len(self.ljono):

                self.ljono.extend(self._luo_lista(self.kasvatuskoko))

            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            return True

        return False

    def poista(self, n):

        try:
            index = self.ljono.index(n, 0, self.alkioiden_lkm)
            self.ljono.pop(index)
            self.ljono.append(0)
            self.alkioiden_lkm -= 1
            return True

        except ValueError as poistovirhe:
            # Selkeät error-messaget helpottaa
            print("Virhe havaittu poistamisen yhteydessä:", poistovirhe)
            return False

    def kopioi_lista(self, a, b):
        for i in range(len(a)):
            b[i] = a[i]

    def joukon_koko(self):
        # ? mahtavuus ? --> joukon_koko
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        for numero in a.to_int_list() + b.to_int_list():
            x.lisaa(numero)
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        for numero in a_taulu:
            if b.kuuluu(numero):
                y.lisaa(numero)
        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        for numero in a.to_int_list():
            if not b.kuuluu(numero):
                z.lisaa(numero)
        return z

    def __str__(self):
        alkiot = self.to_int_list()
        if not alkiot:
            return "{}"
        return "{" + ", ".join(str(alkio) for alkio in alkiot) + "}"

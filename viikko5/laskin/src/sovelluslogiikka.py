class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._komento_ketju = []

    def miinus(self, operandi):
        self._komento_ketju.append((self._arvo, 'EROTUS'))
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._komento_ketju.append((self._arvo, 'SUMMA'))
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._komento_ketju.append((self._arvo, 'NOLLAUS'))
        self._arvo = 0

    def kumoa(self):
        if self._komento_ketju:
            self._arvo, viim_komento = self._komento_ketju.pop()
            return viim_komento

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo

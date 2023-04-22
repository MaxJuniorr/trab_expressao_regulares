import re
from src.common.helper import Reconhecedor


class Alfa(Reconhecedor):
    def __str__(self):
        return "Alfa"

    def reconhecer(self, entrada: str) -> bool:
        """Reconhece casais heterossexuais mais velhos que os filhos com
        pelo menos duas filhas mulheres, ou pelo menos um filho homem, ou
        ainda pelo menos dois filhos homens e uma filha mulher.

        Args:
            entrada {str} -- um arranjo familiar

        Retorna:
            {bool}
        """

        subregra1 = r'(HM)|(MH)'
        subregra2 = r'[hm]*m[hm]*m[hm]*'
        subregra3 = r'[hm]*h[hm]*'
        subregra4 = r'([hm]*h[hm]*h[m]*|[hm]*h[m]*h[hm]*|[m]*h[hm]*h[hm]*)'
        regra = fr"^({subregra1})({subregra2}|{subregra3}|{subregra4})$"
        reconhecido = re.search(regra, entrada)
        return bool(reconhecido)


class Beta(Reconhecedor):
    def __str__(self):
        return "Beta"

    def reconhecer(self, entrada: str) -> bool:
        pass


class Charlie(Reconhecedor):
    def __str__(self):
        return "Charlie"

    def reconhecer(self, entrada: str) -> bool:
        pass


class Delta(Reconhecedor):
    def __str__(self):
        return "Delta"

    def reconhecer(self, entrada: str) -> bool:
        pass


class Echo(Reconhecedor):
    def __str__(self):
        return "Echo"

    def reconhecer(self, entrada: str) -> bool:
        pass


class Foxtrot(Reconhecedor):
    def __str__(self):
        return "Foxtrot"

    def reconhecer(self, entrada: str) -> bool:
        pass


class Golf(Reconhecedor):
    def __str__(self):
        return "Golf"

    def reconhecer(self, entrada: str) -> bool:
        pass

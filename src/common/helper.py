class Reconhecedor:
    """Classe abstrata para descrever os contextos (regras) de
    reconhecimento de uma entrada.
    """

    def reconhecer(self, entrada: str):
        pass


class Verificador:
    """Classe para implementar um reconhecedor específico."""
    def __init__(self, reconhecedor: Reconhecedor):
        self.reconhecedor = reconhecedor

    def reconhecer(self, entrada: str) -> bool:
        return self.reconhecedor.reconhecer(entrada)

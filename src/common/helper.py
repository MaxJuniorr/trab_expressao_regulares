from abc import ABC, abstractmethod


class Reconhecedor(ABC):
    """Classe abstrata para descrever os contextos (regras) de
    reconhecimento de uma entrada.
    """

    @abstractmethod
    def reconhecer(self, entrada: str):
        """Método abstrato para reconhecer uma entrada."""
        pass


class Verificador:
    """Classe concreta para implementar um reconhecedor específico."""
    def __init__(self, reconhecedor: Reconhecedor):
        self.reconhecedor = reconhecedor

    def reconhecer(self, entrada: str) -> bool:
        """Método concreto para reconhecer uma entrada."""
        return self.reconhecedor.reconhecer(entrada)

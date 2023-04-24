from typing import Callable
import re


def verificador(regra: str) -> Callable[[str], bool]:
    """Recebe uma regra de produção e retorna uma função que
    verifica se uma cadeia de caracteres está dentro dessa regra.
    
    Args:
        regra {str} -- uma regra de produção
    
    Returns:
        Callable[[str], bool] -- uma função que recebe uma cadeia de
        caracteres e retorna um booleano
    """
    
    def verifica(cadeia: str) -> bool:
        """Verifica se uma cadeia de caracteres está dentro de uma
        regra de produção.
        
        Args:
            cadeia {str} -- uma cadeia de caracteres
        
        Returns:
            bool -- True se a cadeia está dentro da regra, False caso
            contrário
        """
        
        match = re.search(regra, cadeia)
        return bool(match)
    
    return verifica

def main():
    # Exemplo: Criando um reconhecedor de emails
    email = verificador(r"[a-z]+@[a-z]+(\.com)?\.br")
    # Aplicando o reconhecedor
    print(email('aluno@ufpa.br'))

if __name__ == '__main__':
    main()
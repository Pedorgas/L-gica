
def soma_dobro(valor_a, valor_b):
    '''
    param valor_a: um valor inteiro
    param valor_b: um valor inteiro
    returns: um valor inteiro

    Sendo dois números inteiros (valor_a e valor_b) retorna a soma dos dois
    valores. Porém, se os dois números forem iguais, deve retornar o dobro
    da soma.

    Ex.
    soma_dobro(1, 2) -> 3, porque 1 + 2 = 3
    soma_dobro(2, 2) -> 8, porque (2 + 2) * 2 = 8
    '''
    if valor_a == valor_b:
        return (valor_a + valor_b) * 2
    else:
        return valor_a + valor_b

def diff21(n):
    """
    param n: um valor inteiro
    returns: um valor inteiro

    Sendo um inteiro 'n', deve retornar a diferença absoluta entre 'n' e 21.
    Porém, se o número 'n' for maior que 21, deve retornar o dobro da
    diferença absoluta

    Ex.
    diff21(19) -> 2, porque 21 - 19 = 2
    diff21(25) -> 8, porque (25 - 21) * 2 = 4 * 2 = 8
    """
    if n > 21:
        sub= n - 21
        multip = sub * 2
        return multip
    else:
        sub = 21 - n 
        return sub

def dez(valor_a, valor_b):
    """
    param valor_a: um número inteiro
    param valor_b: um númeri inteiro
    returns: um valor True ou False

    Sendo dois inteiros valor_a e valor_b, deve retornar True se
    um dos dois valores for 10 ou se a soma dos dois valores for 10

    Ex.
    dez(10, 8) -> True
    dez(5, 6) -> False
    dez(2, 8) -> True
    """
    if valor_a == 10 or valor_b == 10:
        return True
    elif valor_a + valor_b == 10:
        return True
    else:
        return False

def menor_preco(p1, p2, p3):
    '''
    param p1: um valor de preço 1, em formato float
    param p2: um valor de preço 2, em formato float
    param p2: um valor de preço 3, em formato float
    returns: o menor dos preços, na lista informada.

    Receba o  preço de três produtos e retorne o menor preço.
    Os três preços são diferentes.

    Exemplo:
        se forem informados os valores, p1=10.0, p2=2.50, p3=25,
        o programa deve devolver o valor 2.50.

    Não utilize nenhuma função de ordenação, apenas if-elif-else.'''
    if p1 < p2 and p1 < p3:
        return p1
    elif p2 < p1 and p2 < p3:
        return p2
    else:
        return p3

def troca_caixa(texto):
    """
    param texto: uma string
    returns: uma strings

    Deve retornar o próprio texto, com as vogais em caixa alta (maiúsculas), e
    as consoantes em caixa baixa (minúsculas)

    Ex.
    troca_caixa('instituto') -> 'InstItUtO'
    """
    texto= texto.lower()
    texto=texto.replace("a","A")
    texto=texto.replace("e","E")
    texto=texto.replace("i","I")
    texto=texto.replace("o","O")
    texto=texto.replace("u","U")
    return texto



# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' % ('Falhou')
    else:
        prefixo = '\033[32m%s' % ('Passou')
        acertos += 1
    print('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado),
                                                    repr(obtido)))


def main():
    print('Soma dobro')
    test(soma_dobro(1, 2), 3)
    test(soma_dobro(3, 2), 5)
    test(soma_dobro(2, 2), 8)
    test(soma_dobro(-1, 0), -1)
    test(soma_dobro(0, 0), 0)
    test(soma_dobro(0, 1), 1)

    print('Diff21')
    test(diff21(19), 2)
    test(diff21(10), 11)
    test(diff21(21), 0)
    test(diff21(22), 2)
    test(diff21(25), 8)
    test(diff21(30), 18)

    print('Dez')
    test(dez(9, 10), True)
    test(dez(9, 9), False)
    test(dez(1, 9), True)
    test(dez(10, 1), True)
    test(dez(10, 10), True)
    test(dez(8, 2), True)
    test(dez(8, 3), False)
    test(dez(10, 42), True)
    test(dez(12, -2), True)

    print('Menor preço:')
    test(menor_preco(1, 2, 3), 1)
    test(menor_preco(1, 3, 2), 1)
    test(menor_preco(2, 1, 3), 1)
    test(menor_preco(2, 3, 1), 1)
    test(menor_preco(3, 1, 2), 1)
    test(menor_preco(3, 2, 1), 1)

    print(' Troca caixa:')
    test(troca_caixa("Araquari"), "ArAqUArI")  # normal
    test(troca_caixa("Caxias do Sul"), "cAxIAs dO sUl")  # com espaços


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (
        total, acertos, total - acertos, float(acertos * 10) / total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")

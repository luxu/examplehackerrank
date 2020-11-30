# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    """
    Function que testa qtos pares de meias foram vendidos
    :param n: int
    :param ar: int
    :return: int
    >>> sockMerchant(9, [1,1,3,1,2,1,3,3,3,3])
    4
    """
    qtd = 0
    cont = 0
    for cor in ar:
        print(cor, ar[cont])
        aux = cor
        if aux == ar[cont]:
            qtd += 1
            cont += 1
    return qtd

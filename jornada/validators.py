from djmoney.money import Money

def preco_invalido(preco):
    """Valida se o preço é maior ou igual a 100 BRL"""
    if isinstance(preco, Money):
        preco = preco.amount  
    return preco < 100 or preco > 30000  
    
def nome_invalido(nome):
    return not nome.isalpha()


import requests

#funcao para calcular a media ponderada e a media simples de tres notas
def calcular_media(n1, n2, n3):
    media_ponderada = (n1 * 0.3 + n2 * 0.3 + n3 * 0.4) / (0.3 + 0.3 + 0.4)
    media = (n1 + n2 + n3) / 3
    return media_ponderada, media

#Função para obter a cotação do dólar em tempo real
def obter_cotacao_dolar():
    cotacao_reserva = 5.50
    try:
        requisicao = requests.get(" https://economia.awesomeapi.com.br/last/USD-BRL", timeout=5) 
        requisicao.raise_for_status()
        return float(requisicao.json()['USDBRL']['bid'])  # Verifica se a requisição foi bem-sucedida

    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Erro ao obter a cotação do dólar: {e}")
        return cotacao_reserva  # Retorna a cotação de reserva em caso de erro

#Função para obter a cotação da libra em tempo real
def obter_cotacao_libra():
    cotacao_reserva = 7.00
    try:
        requisicao = requests.get(" https://economia.awesomeapi.com.br/last/GBP-BRL", timeout=5) 
        requisicao.raise_for_status()
        return float(requisicao.json()['GBPBRL']['bid']) 

    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Erro ao obter a cotação da libra: {e}")
        return cotacao_reserva  # Retorna a cotação de reserva em caso de erro


#Função para obter a cotação do euro em tempo real
def obter_cotacao_euro():
    cotacao_reserva = 6.00
    try:
        requisicao = requests.get(" https://economia.awesomeapi.com.br/last/EUR-BRL", timeout=5) 
        requisicao.raise_for_status() # Verifica se a requisição foi bem-sucedida
        return float(requisicao.json()['EURBRL']['bid']) 

    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Erro ao obter a cotação do euro: {e}")
        return cotacao_reserva  # Retorna a cotação de reserva em caso de erro

#funcao para converter reais para euros
def converter_real_para_euro(valor_real):
    cotacao_euro = obter_cotacao_euro()
    valor_euro = valor_real / cotacao_euro
    return f"O {valor_real} BRL inserido é equivalente a {valor_euro:.2f} EUR"


#funcao para converter reais para dolares
def converter_real_para_dolar(valor_real):
    cotacao_dolar = obter_cotacao_dolar()
    valor_dolar = valor_real / cotacao_dolar
    return f"O {valor_real} BRL inserido é equivalente a {valor_dolar:.2f} USD"

#funcao para converter reais para libras
def converter_real_para_libra(valor_real):
    cotacao_libra = obter_cotacao_libra()
    valor_libra = valor_real / cotacao_libra
    return f"O {valor_real} BRL inserido é equivalente a {valor_libra:.2f} GBP"

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b): 
    return a * b

def divisao(a, b):
    if a == 0 or b == 0:
        raise ValueError("Erro: Divisão por zero não é permitida.")
    
    return a / b, a // b, a % b

def potencia(a, b):
    return a ** b

def raiz(a, b):
    raiz = pow(a, 1/b)
    return raiz

import requests
import math

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

#funcao para somar 2 valores
def soma(a, b):
    return a + b

#funcao para subtrair 2 valores
def subtracao(a, b):
    return a - b

#funcao para multiplicar 2 valores
def multiplicacao(a, b): 
    return a * b

#funcao para dividir 2 valores e retornar o quociente, inteiro e resto
def divisao(a, b):
    if a == 0 or b == 0:
        raise ValueError("Erro: Divisão por zero não é permitida.")
    else:
        quociente = a / b
        inteiro = a // b
        resto = a % b
        return f"Quociente: {quociente}, Inteiro: {inteiro}, Resto: {resto}"

#funcao para calcular a potencia de um valor
def potencia(a, b):
    return a ** b

#funcao para calcular a raiz de um valor
def raiz(a, b):
    raiz = math.pow(a, 1/b)
    return raiz 

#funcao para converter temperatura de Celsius para Fahrenheit 
def converte_para_fahrenheit(temperatura):
    fahrenheit = (temperatura * 9/5) + 32
    return f"A temperatura {temperatura}°C em Fahrenheit é: {fahrenheit:.2f} °F"

#funcao para converter temperatura de Celsius para Kelvin
def converter_para_kelvin(temperatura):
    kelvin = temperatura + 273.15
    return f"A temperatura {temperatura}°C em Kelvin é: {kelvin:.2f} K"

def mostrar_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return f"O antecessor de {numero} é {antecessor} e o sucessor é {sucessor}."

def trocar_com_pythonico(a, b):
    a, b = b, a
    return f"variavel 1: ({a}), variavel 2: ({b})"

def trocar_com_auxiliar(a, b):
    auxiliar = a
    a = b
    b = auxiliar
    return a, b

def identificar_tipo(valor):
    """Recebe uma string e tenta convertê-la para int, depois float, senão mantém como str."""
    try:
        return int(valor)
    except ValueError:
        try:
            return float(valor)
        except ValueError:
            return valor  # continua como str
    
def valor_lucro_venda(preco_compra, preco_lucro):
    valor_lucro = preco_compra * (preco_lucro / 100)
    preco_venda = preco_compra + valor_lucro
    return f"O preço de venda do produto é: {preco_venda:.2f} BRL, sendo o lucro de {valor_lucro:.2f} BRL."

def calcular_area_circulo(raio):
    area = math.pi * (raio ** 2)
    return f"A área do círculo com raio {raio} é: {area:.2f} cms²."

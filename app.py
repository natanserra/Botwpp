import openpyxl
import pyperclip
import pyautogui
from time import sleep

def copiar_e_colar(valor, posicao, clicado=False):
    pyperclip.copy(valor)
    if clicado:
        pyautogui.click(posicao[0], posicao[1], duration=1)
    pyautogui.hotkey('ctrl', 'v')

def selecionar_tamanho(tamanho):
    tamanho_map = {
        'Pequeno': (1520, 705),
        'Médio': (1509, 730)
    }
    posicao = tamanho_map.get(tamanho, (1503, 748))
    pyautogui.click(1530, 670, duration=1)
    pyautogui.click(posicao[0], posicao[1], duration=1)

# Carregar dados
workbook = openpyxl.load_workbook('clientes.xlsx')
sheet_produtos = workbook['Produtos']

# Iterar sobre as linhas do Excel
for linha in sheet_produtos.iter_rows(min_row=2):
    campos = [
        ('nome_produto', (1518, 305)),
        ('descricao', (1472, 413)),
        ('categoria', (1467, 526)),
        ('codigo_produto', (1481, 614)),
        ('peso', (1463, 691)),
        ('dimensoes', (1465, 783)),
        ('preco', (1539, 325)),
        ('quantidade_em_estoque', (1515, 411)),
        ('data_de_validade', (1504, 501)),
        ('cor', (1489, 574)),
        ('material', (1482, 753)),
        ('fabricante', (1465, 347)),
        ('pais_origem', (1473, 426)),
        ('observacoes', (1475, 523)),
        ('codigo_de_barras', (1471, 655)),
        ('localizacao_armazem', (1472, 733))
    ]
    
    for idx, (campo, posicao) in enumerate(campos):
        valor = linha[idx].value
        copiar_e_colar(valor, posicao, clicado=True)
        sleep(1)  


    tamanho = linha[10].value
    selecionar_tamanho(tamanho)

    pyautogui.click(1494, 808, duration=1)
    sleep(1)
    pyautogui.click(1887, 198, duration=1)
    pyautogui.click(1886, 191, duration=1)
    pyautogui.click(1695, 580, duration=1)

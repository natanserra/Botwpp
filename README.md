Instruções para Utilização do Programa de Automação de Mensagens de WhatsApp
Requisitos
Python: Certifique-se de que o Python está instalado no seu sistema. Você pode baixá-lo de python.org.

Bibliotecas Necessárias: O programa utiliza as bibliotecas openpyxl, pyperclip, e pyautogui. Você precisa instalá-las se ainda não estiverem instaladas.

Passo 1: Instalar Bibliotecas
Abra o terminal ou prompt de comando.

Execute os seguintes comandos para instalar as bibliotecas necessárias:

python -m pip install openpyxl pyperclip pyautogui
Passo 2: Preparar o Arquivo Excel
Crie ou obtenha um arquivo Excel: O arquivo deve ser no formato .xlsx e deve conter as seguintes colunas (em ordem):

Nome do Produto
Descrição
Categoria
Código do Produto
Peso
Dimensões
Preço
Quantidade em Estoque
Data de Validade
Cor
Tamanho
Material
Fabricante
País de Origem
Observações
Código de Barras
Localização do Armazém
Nome do Arquivo: Salve o arquivo com o nome produtos_ficticios.xlsx ou ajuste o nome no código conforme necessário.

Coloque o Arquivo: Certifique-se de que o arquivo está no mesmo diretório que o script Python ou ajuste o caminho no código para corresponder à localização do arquivo.

Passo 3: Preparar o Ambiente
Abra o Aplicativo de Destino: Abra o aplicativo onde você deseja colar as informações (por exemplo, uma interface de administração de produtos no WhatsApp Web).

Posicione o Aplicativo: Coloque a janela do aplicativo em uma posição fixa e maximize-a se necessário. O script usa coordenadas fixas para clicar e colar, então a posição da janela deve ser consistente com as coordenadas no código.

Passo 4: Executar o Script
Salve o Código: Salve o código Python em um arquivo com a extensão .py, por exemplo, automacao_whatsapp.py.

Execute o Script: Abra o terminal ou prompt de comando, navegue até o diretório onde o script está salvo e execute:
python automacao_whatsapp.py
Acompanhe a Execução: O script começará a processar as informações do arquivo Excel e preencher os campos no aplicativo de destino. Acompanhe a execução para garantir que tudo esteja funcionando corretamente.

Dicas e Ajustes
Ajuste de Coordenadas: Se as coordenadas não estiverem corretas para o seu aplicativo, você pode usar uma ferramenta de captura de coordenadas de tela ou ajustar manualmente as coordenadas no código.

Tempos de Espera: Se o aplicativo for lento para responder, você pode aumentar o tempo de espera (sleep) entre as ações para garantir que o aplicativo tenha tempo suficiente para processar cada ação.

Tratamento de Erros: Verifique se há erros no terminal e ajuste o código conforme necessário. Se um erro ocorrer, revise as mensagens de erro e ajuste o código ou a configuração do aplicativo.

import pywhatkit as kit
import time

def validar_numero(numero):
    """
    Valida o formato do número de telefone.
    
    :param numero: Número de telefone.
    :return: Booleano indicando se o número é válido.
    """
    import re
    padrao = re.compile(r"^\+\d{11,15}$")  # Ajuste conforme necessário para seu formato
    return padrao.match(numero) is not None

def enviar_mensagem_imediata(numero, mensagem):
    """
    Envia uma mensagem no WhatsApp imediatamente.
    
    :param numero: Número de telefone no formato internacional.
    :param mensagem: Mensagem a ser enviada.
    """
    try:
        if not validar_numero(numero):
            raise ValueError("Número de telefone inválido. Certifique-se de usar o formato correto.")

        # Enviar a mensagem
        kit.sendwhatmsg_instantly(numero, mensagem)
        print(f"Mensagem enviada imediatamente para {numero}.")
    
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():
    numero = input("Digite o número de telefone no formato internacional (ex: +5511999999999): ")
    mensagem = input("Digite a mensagem a ser enviada: ")
    
    enviar_mensagem_imediata(numero, mensagem)

if __name__ == "__main__":
    main()

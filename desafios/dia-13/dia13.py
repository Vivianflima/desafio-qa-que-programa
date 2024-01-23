import re

def validar_email(email):
    # Definir a expressão regular para validar o e-mail
    padrao_email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    # Verificar se o e-mail corresponde ao padrão
    return padrao_email.match(email) is not None

# Solicitar ao usuário inserir um e-mail
email_usuario = input("Digite seu e-mail: ")

# Validar o e-mail fornecido pelo usuário
if validar_email(email_usuario):
    print(f'O e-mail "{email_usuario}" é válido.')
else:
    print(f'O e-mail "{email_usuario}" é inválido.')


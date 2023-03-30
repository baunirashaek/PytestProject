def checarLogin(username):

    if not username[0].isupper():
        print("O nome de usuário deve ter letra maiúscula!")
        return None
    if any(not c.isalnum() for c in username):
        print("Nome de usuário não pode ter caracteres especiais!")
        return None
    if len(username) > 30:
        print("Nome de usuário deve ter até 30 caracteres!")
        return None
    else:
        return username


def checarSenha(senha):
    num = ['1','2','3','4','5','6','7','8','9','0']
    if len(senha) < 10:
        print("A senha deve ter pelo menos 10 caracteres!")
        return None
    if not any(not c.isalnum() for c in senha):
        print("Precisa ter pelo menos um caractere especial!")
        return None
    if not any(i.isdigit() for i in senha):
        print("A senha precisa ter pelo menos um número!")
        return None
    if not any(char.isupper() for char in senha):
        print("A senha deve ter pelo menos UMA letra MAIÚSCULA!")
        return None
    if not any(char.islower() for char in senha):
        print("A senha deve ter pelo menos UMA letra MINÚSCULA!")
        return None
    else:
        return senha

def checarMensagem(mensagem):
    if len(mensagem) > 70:
        print(f"A mensagem deve ter no máximo 70 caracteres. Você digitou {len(mensagem)} caracteres.")
        return None
    else:
        return mensagem

def pedirLogin():
    username = input("Insira o seu username: ")
    username = checarLogin(username)
    
    senha = input("Insira sua senha: ")
    senha = checarSenha(senha)

    if username != None:
        print("Tudo certo com username.")
    if senha != None:
        print("Tudo certo com a senha.")

    if username != None and senha != None:
        pedirMensagem()

def pedirMensagem():
    mensagem = input("Insira a mensagem desejada: ")
    mensagem = checarMensagem(mensagem)
    if mensagem != None:
        print("Tudo certo com a mensagem.")
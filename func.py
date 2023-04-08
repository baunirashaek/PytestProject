from cryptographyFramework import *


def init_encrypt(username, senha, mensagem):
    u = checarLogin(username)
    s = checarSenha(senha)
    m = checarMensagem(mensagem)
    if u != None and s != None and m != None:
        encryptMessage(username, senha, mensagem)
        return True
    else:
        return False 


def checarLogin(username):
    if checarLenMin(username):
        if checarUpper(username) and checarCarSpec(username) and checarLen(username):
            return username
        else:
            return None
    else:
        return None

def checarUpper(username):
    if username[0].isupper():
        return True
    else:
        return False

def checarCarSpec(username):
    if any(not c.isalnum() for c in username):
        return False
    else:
        return True

def checarLen(username):
    if len(username) < 31:
        return True
    else:
        return False

def checarLenMin(username):
    if len(username) > 0:
        return True
    else:
        return False

def checarSenha(senha):
    if checarLenSenha(senha) and checarCarSpecSenha(senha) and checarNumSenha(senha) and checarAnyUpperSenha(senha) and checarAnyLowerSenha(senha):
        return senha
    else:
        return None

def checarLenSenha(senha):
    if len(senha) > 9:
        return True
    else:
        return False

def checarCarSpecSenha(senha):
    if any(not c.isalnum() for c in senha):
        return True
    else:
        return False

def checarNumSenha(senha):
    if any(i.isdigit() for i in senha):
        return True
    else:
        return False

def checarAnyUpperSenha(senha):
    if any(char.isupper() for char in senha):
        return True
    else:
        return False

def checarAnyLowerSenha(senha):
    if any(char.islower() for char in senha):
        return True
    else:
        return False

def checarMensagem(mensagem):
    if checarLenMensagem(mensagem):
        return mensagem
    else:
        return None

def checarLenMensagem(mensagem):
    if len(mensagem) < 71:
        return True
    else:
        return False

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